<?php
    session_start();


    if (isset($_POST['nick'])) {

        $complete = true; #jeżeli w całym pliku to idziemy dalej

        #wymagany zakres długości nicku
        if ((strlen($_POST['nick'])) < 4 || (strlen($_POST['nick'])) > 15) {
            $complete = false;
            $_SESSION['error_nick'] = "Nick must contain between 4 and 15 chars";
        }

        #bez dziwnych znaków w nicku
        if (ctype_alnum($_POST['nick']) == false) {
            $complete = false;
            $_SESSION['error_nick'] = "Only chars and digits are accepted";
        }

        #wymagany zakres długości hasła
        if ((strlen($_POST['pswd1']) < 6) || (strlen($_POST['pswd1']) > 15)) {
            $complete = false;
            $_SESSION['error_pswd'] = "Password must contain between 6 and 15 chars";
        }

        #hasło powtórne musi być takie samo
        if ($_POST['pswd1'] != $_POST['pswd2']) {
            $complete = false;
            $_SESSION['error_pswd'] = "Passwords aren`t the same";
        }

        #hashowanie hasła
        $password_hash = password_hash($_POST['pswd1'], PASSWORD_DEFAULT);

        #akceptacja ragulaminu
        if (!isset($_POST['regulations'])) {
            $complete = false;
            $_SESSION['error_regulations'] = "Regulations must be accepted";
        }

        #to do recaptchy (generowane przez google)
        $hidden = "6LcPpFQUAAAAAOXTviam8G7v9is9wtR8O38Z2Ln8";
        $check = file_get_contents('https://www.google.com/recaptcha/api/siteverify?secret=' . $hidden . '&response=' . $_POST['g-recaptcha-response']);
        $answer = json_decode($check);

        #rozwiazywanie re-captchy
        if ($answer->success == false) {
            $complete = false;
            $_SESSION['error_bot'] = "Solve re-captcha";
        }

        require_once "connect.php";

        #rzucanie wyjątków
        mysqli_report(MYSQLI_REPORT_STRICT);

        try
        {
            #połączenie z bazą danych
            $connection = new mysqli($host, $db_user, $db_password, $db_name);

            if ($connection->connect_errno!=0)
            {
                throw new Exception(mysqli_connect_errno());
            }
            else
            {
                #w przypadku wykrycia współbierzności nicków
                $nick = $_POST['nick'];
                $result = $connection->query("SELECT id FROM users WHERE user='$nick'");

                if (!$result)
                    throw new Exception($connection->error);

                if($result->num_rows > 0)
                {
                    $complete = false;
                    $_SESSION['error_nick'] = "This nickname is already exists";
                }


                #jeśli wszystko ok to INSERT
                if($complete == true)
                {
                    if($connection->query("INSERT INTO users VALUES (NULL,'$nick','$password_hash')"))
                    {
                        #echo "udalo sie";

                        $_SESSION['signedup'] = true;
                        header('Location: index.php');
                    }
                    else
                    {
                        #echo "nie udalo sie";
                        throw new Exception($connection->error);
                    }
                }

                $connection->close();

            }
        }
        catch (Exception $e)
        {
            # w przypadku błędów w połączeniu informacja
            # echo "Serwer error";
        }

    }

?>




<!DOCTYPE HTML>
<html lang="pl">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <link rel="stylesheet" href="FilesCSS/main.css">
    <title>Stack UnderFlow - rejestracja</title>
    <script src='https://www.google.com/recaptcha/api.js'></script>
</head>

<body>
<img id="Logo" src="img/Logo.gif">
    <div class="Window">
        <header>
           <h1>Signing up</h1>
        </header>

        <main>
            <form method = "post">
                <h2>Nickname:</h2>
                <input type = "text" name = "nick" /><br/>

                <!-- wyświetlanie informacji o errorze gdy któreś z pól nie spełnia zależności -->
                <?php

                if (isset($_SESSION['error_nick']))
                {
                    echo '<div class = "error">'.$_SESSION['error_nick'].'</div>';
                    unset($_SESSION['error_nick']);
                }
                ?>

                <h2>Password:</h2>
                <input type = "password" name = "pswd1" /><br/>

                <?php

                if (isset($_SESSION['error_pswd']))
                {
                    echo '<div class = "error">'.$_SESSION['error_pswd'].'</div>';
                    unset($_SESSION['error_pswd']);
                }
                ?>

                <h2>Repeat Password:</h2>
                <input type = "password" name = "pswd2" /><br/>

                <br/>

                <label>
                    <input type = "checkbox" name = "regulations" />
                    <button onclick="myFunction()">Regulations</button>
                    <script>
                        function myFunction() {
                            window.open("regulamin.txt","","top = 500,left = 600,width=200,height=100");
                        }
                    </script>
                </label>

                <?php

                if (isset($_SESSION['error_regulations']))
                {
                    echo '<div class = "error">'.$_SESSION['error_regulations'].'</div>';
                    unset($_SESSION['error_regulations']);
                }
                ?>

                <br/><br/>

                <div class="g-recaptcha" data-sitekey="6LcPpFQUAAAAAMLZSVgNpuauDRoGXymZwKRy-grm"></div>

                <?php

                if (isset($_SESSION['error_bot']))
                {
                    echo '<div class = "error">'.$_SESSION['error_bot'].'</div>';
                    unset($_SESSION['error_bot']);
                }
                ?>

                <br/>

                <input type = "submit" value = "Finish!" />

            </form>
        </main>
    </div>
</body>
</html>