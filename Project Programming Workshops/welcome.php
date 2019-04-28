<?php

session_start();

if (isset($_SESSION['signedup']))
{
    header('Location: index.php');
    exit();
}
else
{
    unset($_SESSION['signedup']);
}

?>

<!DOCTYPE HTML>
<html lang="pl">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <title>Osadnicy - gra przeglądarkowa</title>
</head>

<body>

Dziekujemy za rejestracje w serwisie, mozesz juz zalogowac sie na swoje konto!<br /><br />

<a href = "index.php">Zaloguj sie na swoje konto!</a>
<br/><br/>

</body>
</html>