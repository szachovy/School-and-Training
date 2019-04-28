

<!DOCTYPE HTML>
<html lang="pl">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <link rel="stylesheet" href="FilesCSS/forum.css">
    <title>Stack Under Flow - sign in</title>
    <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
    <![endif]-->
</head>

<body>

<h1>Question</h1>
<h2>
<?php
session_start();
require_once "connect.php";

#zfetchowanie danych w zależności od wybranej dyskusji
$id = $_GET['id'];

$connection = @new mysqli($host, $db_user, $db_password, $db_name);
    if($result = $connection->query("SELECT * FROM ctopics WHERE id = $id"))
    {

        $row = $result->fetch_assoc();
        echo "From : ".$row['user'];
        echo '<br/><br/>';
        echo $row['topic'];
    }
$connection->close();
?>
</h2>

<h1>Discussion</h1>
<form style="font-style:italic;font-weight: bold;text-align: center" method="post">
    <?php
    $fp = @fopen('ctxt/'.$id.".txt", 'r');

    # Sprawdzamy rozmiar pliku
    $size = @filesize('ctxt/'.$id.".txt");

    # Odczytujemy treść pliku
    $log = @fread( $fp, $size );

    # Tworzymy tablicę z logami
    $log = explode("\n", $log);

    # Każdy element tablicy dzielimy na komórki z poszczególnymi danymi
    foreach($log as &$element)
        $element = explode("||", $element);

    # Definiujemy funkcję array_column
    if(!function_exists("array_column"))
    {
        function array_column($array,$column_name)
        {
            return array_map(function($element) use($column_name){return $element[$column_name];}, $array);
        }
    }

    # Pobieramy kolumnę z zawartością do jednej tablicy
    $content = array_column($log, 0);

    # Usuwamy duplikaty
    $content = array_unique($content);

    # Wypisujemy tablice
    foreach ($content as $line_num => $line) {
        if(!empty($line)) {
            echo htmlspecialchars($line).'</br>'.'</br>'.'</br>';
        }
    }
    ?>
    <textarea name="textc" rows="10" cols="30"></textarea>
    <br/><br/>
    <input name="sumbit" type="submit" value="Sumbit" style="width: 20%;color: blueviolet"/>
</form>

<?php
#zapisujemy textaree do pliku txt
if(isset($_POST['textc']) && isset($_POST['sumbit']) && !empty($_POST))
{
    $text = $_POST['textc'].PHP_EOL;
    if($fp = @fopen('ctxt/'.$id.'.txt',"a")) {
        flock($fp, 2);
        fwrite($fp, $text);
        flock($fp, 3);
        fclose($fp);
        unset($_POST['textc']);
        unset($_POST['sumbit']);
    }
}
?>

<!-- powrót do strony z tematami-->
<a href="C.php"><img src="FilesCSS/img/back.png" width="350"/></a>
</body>
</html>
