
<!DOCTYPE HTML>
<html lang="pl">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <link rel="stylesheet" href="FilesCSS/topics.css">
    <title>Stack Under Flow - sign in</title>
    <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
    <![endif]-->
</head>

<body>

<?php
#informacja o błędzie w razie nie wpisania danych
session_start();
if(isset($_SESSION['err']))
    echo '<span style="color:red">Error with selecting language or typing textarea</span>';
unset($_SESSION['err'])
?>

<img id="Logo" src="FilesCSS/img/Logo.gif">

<h1>Select Your Programing language</h1>

<!-- form którego obsługa znajduje się w lang.php -->
<div class="choose">
    <form action="lang.php" method="post" >
        <input list="options" name="options">
        <datalist id="options">
            <option value="C/C++" name="C/C++">
            <option value="Python" name="Python">
            <option value="Java" name="Java">
            <option value="PHP" name="PHP">
        </datalist>
        <h2 style="margin-right: 15%">Express what do you need to know</h2>
        <textarea name="message" style="width:70%; height:200px;margin-left:25% "></textarea>
        <br/><br/><br/><br/><br/><br/>
        <input type="submit" value="Sumbit" style="width: 30%;color: blueviolet">
    </form>
</div>

<a href="C.php"><img src="FilesCSS/img/back.png" width="350"/></a>
</body>
</html>
