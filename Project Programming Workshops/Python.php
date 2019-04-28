<?php

session_start();

#nie ma możliwości przejść do tej strony gdy nie jest sie zalogowanym
if (!isset($_SESSION['signedin']))
{
    header('Location: index.php');
    exit();
}

#dla powitania
$login =  $_SESSION['login'];
?>

<!DOCTYPE HTML>
<html lang="pl">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <link rel="stylesheet" href="FilesCSS/forum.css">
    <title>Stack Under Flow</title>
    <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
    <![endif]-->
</head>

<body>
<div align="left">
    <img id="Logo" src="FilesCSS/img/Logo.gif">
</div>
<?php
#powitanie
echo "<div class='greetings'>Good Morning $login</div>"
?>
<!-- przycisk do wylogowania sie -->
<a href="logout.php" style="width: 30px;height: 30px;margin-left: 80%;"><img src="FilesCSS/img/logout.png" width="150"/></a>

<!-- przycisk do tworzenia wlasnego wątku -->
<div align="center">
    <a href="Create.php"><img src="FilesCSS/img/create.png" width="350"/></a>
</div>

<!-- linki do pozostałych dyskusji -->
<ul>
    <li><a href="C.php">C/C++ language</a></li>
    <li><a href="Python.php">Python language</a></li>
    <li><a href="Java.php">Java language</a></li>
    <li><a href="PHP.php">PHP and other web elements</a></li>
</ul>
<?php

#wypisywanie wszystkich danych z tematów z danego języka z odpowiedniej bazy danych
#fetchowanie całej bazy jako tabeli z danego języka
#i wypisywanie wiersz po wierszu

require_once "connect.php";
$connection = @new mysqli($host, $db_user, $db_password, $db_name);
if ($result = $connection->query("SELECT * FROM pytopics"))
{

    $amount = $result->num_rows;
    $n = 1;

    echo '<table style="border: 1mm ridge blue;border-collapse: collapse; width: 100%;background: linear-gradient(royalblue, lightblue);">
    <tr style="border: 1mm ridge slateblue">
        <th style="font-size: x-large;font-style: italic; font-weight: bolder;color: darkred;text-shadow: 0 0 3px blue;">id</th>
        <th style="font-size: x-large;font-style: italic; font-weight: bolder;color: darkred;text-shadow: 0 0 3px blue;">user</th>
        <th style="font-size: x-large;font-style: italic; font-weight: bolder;color: red;text-shadow: 0 0 3px blue;">topic</th>
        <th style="font-size: x-large;font-style: italic; font-weight: bolder;color: darkred;text-shadow: 0 0 3px blue;">discussion</th>
    </tr>
    ';while($amount != 0)
{

    echo '<tr/>';
    $row = $result->fetch_assoc();

    echo '<td style="border-right: 1mm ridge blue;font-size:large; padding-left: 0.7%;font-weight: bold;border-bottom: 1mm ridge slateblue;padding-right: 1%;text-underline: blue dash;">';
    echo $row['id'];
    '</td>';
    echo '<td style="border-right: 1mm ridge blue;border-bottom: 1mm ridge slateblue;font-style: italic;">';
    echo $row['user'];
    '</td>';
    echo '<td style="border-bottom: 1mm ridge slateblue;">';
    echo $row['topic'];
    '</td>';

    #link do aktywnej dyskusji
    echo '<td style="border-left: 1mm ridge blue;border-top: 1mm ridge slateblue">';
    echo "<a href=pydiscuss.php?id=$n>forum</a>";
    '</td>';
    echo '<br/><br/>';
    echo '</tr>';

    $amount = $amount - 1;
    $n += 1;
};'
</table>';

}
$connection->close();
?>
</body>
</html>
