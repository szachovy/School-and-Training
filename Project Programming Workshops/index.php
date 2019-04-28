<?php

session_start();

#jeżeli jesteśmy zalogowani to zostaniemy automatycznie przekierowani
if ((isset($_SESSION['signedin'])) && ($_SESSION['signedin']==true))
{
    header('Location: C.php');
    exit();
}
#jeżeli nie jestesmy zalogowani to przechodzimy na strone startowa
#z dostepnym formularzem logowania

?>



<!DOCTYPE HTML>
<html lang="pl">
<head>
    <!--kodowanie znakow-->
    <meta charset="utf-8" />
    <!--kompatybilność z przeglądarkami-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <!--dołączone pliki css-->
    <link rel="stylesheet" href="FilesCSS/main.css">
    <!--tytuł strony-->
    <title>Stack Under Flow - sign in</title>
    <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
    <![endif]-->
</head>

<body>

<img id="Logo" src="img/Logo.gif">
<div class="info">
<main>
    <h2>Made by WJ.Maj<br/>
    PHP Project
    04.2018
    </h2>
</main>
</div>
<div class="Window">
    <header>
        <h1>Sign in</h1>
    </header>

    <main>
        <article>
            <!-- przekierowanie do sign_in.php-->
            <form action="sign_in.php" method="post">

                <!--pola do setowania $_POST['login'] i $_POST['password']-->
                <h2> Login:</h2><input type="text" name="login" /> <br />
                <h2> Password:</h2><input type="password" name="password" /> <br /><br />
                <?php
                #standardowy czerwony napis błędu w przypadku niepoprawnego
                #wprowadzenia danych

                if(isset($_SESSION['error']))
                    echo $_SESSION['error'];
                ?>
                <br/>
                <br/>
                <input type="submit" value="Sign in!" />
                <p>Haven`t got account?
                    <!-- przekierowanie do sign_up.php-->
                    <br/><br/>
                    <a href = "sign_up.php">Sign Up!</a>
                </p>

            </form>
        </article>
    </main>

</div>


</body>
</html>