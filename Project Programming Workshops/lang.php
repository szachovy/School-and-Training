<?php

session_start();

require_once "connect.php";

unset($_SESSION['err']);

$login = $_SESSION['login'];

$selectOption = $_POST['options'];
    #echo $selectOption;
$text =  htmlspecialchars($_POST['message']);
    #echo $text;

#w zależności od wybranych opcji
#zapisujemy dane do odpowiedniej bazy danych
#przy spełnieniu podanych warunków
if((isset($selectOption)) && ($selectOption == "C/C++") && (isset($text)) && (strlen($text) > 0))
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO ctopics VALUES (NULL,'$login','$text')"))
            {
                unset($_SESSION['err']);
                header('Location: C.php');
                xdebug_break();
            }
            else
            {
                #throw błędu jeżeli powstanie
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        #wypisanie wyjątku
        echo $exception;
    }
if((isset($selectOption)) && ($selectOption == "Python")&& (isset($text)) && (strlen($text) > 0))
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO pytopics VALUES (NULL,'$login','$text')"))
            {
                unset($_SESSION['err']);
                header('Location: Python.php');
                xdebug_break();
            }
            else
            {
                #throw błędu jeżeli powstanie
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        #wypisanie wyjątku
        echo $exception;
    }
if((isset($selectOption)) && ($selectOption == "Java")&& (isset($text)) && (strlen($text) > 0))
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO javatopics VALUES (NULL,'$login','$text')"))
            {
                unset($_SESSION['err']);
                header('Location: Java.php');
                xdebug_break();
            }
            else
            {
                #throw błędu jeżeli powstanie
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        #wypisanie wyjątku
        echo $exception;
    }
if((isset($selectOption)) && ($selectOption == "PHP")&& (isset($text)) && (strlen($text) > 0))
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO phptopics VALUES (NULL,'$login','$text')"))
            {
                unset($_SESSION['err']);
                header('Location: PHP.php');
                xdebug_break();
            }
            else
            {
                #throw błędu jeżeli powstanie
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        #wypisanie wyjątku
        echo $exception;
    }
else
{
    #jeżeli nie zostana spełnione wymagane założenia
    $_SESSION['err'] = true;
    header("Location:Create.php");
}

?>