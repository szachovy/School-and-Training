<?php
    session_start();

    #w przypadku gdy dane nie zostały naniesione
    #cofamy sie do index.php
    if ((!isset($_POST['login'])) || (!isset($_POST['password'])))
    {
        header('Location: index.php');
        exit();
    }

    #łączenie z bazą danych (więcej informacji w connect.php)
    require_once "connect.php";

    $connection = @new mysqli($host, $db_user, $db_password, $db_name);

    #w przypadku błędu połączenia
    if ($connection->connect_errno!=0)
    {
        #dostajemy kod błędu który jest wartością zależną
        echo "Error: ".$connection->connect_errno;
    }
    else
    {
        #dla ułatwienia przypisujemy zmiennym wartości z index.php <$_POST[]>
        $login = $_POST['login'];
        $password = $_POST['password'];

        #konwersja znaków
        $login = htmlentities($login, ENT_QUOTES, "UTF-8");

        #zabezpieczenie przed wstrzykiwaniem SQLa
        if ($result = @$connection->query(
            sprintf("SELECT * FROM users WHERE user='%s'",
                mysqli_real_escape_string($connection,$login))))
        {

            #w przypadku błędu należy sprawdzić echo $result->num_rows czy coś sie wyświetla;
            if($result->num_rows > 0)
            {
                #ściąganie danych z bazy "forum"
                $row = $result->fetch_assoc();

                #echo $row['id'].$row['user'].$row['password'];
                #hasła są zahashowane
                if (password_verify($password, $row['password']))
                {
                    $_SESSION['id'] = $row['id'];
                    $_SESSION['login'] = $row['user'];
                    $_SESSION['password'] = $row['password'];


                    $_SESSION['signedin'] = true; #set...

                    unset($_SESSION['error']); #konieczne po ponownym wpisaniu danych
                    $result->free_result();
                    header('Location: C.php');

                }
                else
                {
                    #w przypadku błędu ->password_verify
                    $_SESSION['error'] = '<span style="color:red">Nieprawidłowy login lub hasło!</span>';
                    header('Location: index.php');

                }

            }
            else
            {
                #gdy num_rows = 0
                $_SESSION['error'] = '<span style="color:red">Nieprawidłowy login lub hasło!</span>';
                header('Location: index.php');

            }
        }

        $connection->close();
    }

?>