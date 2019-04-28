<?php
require_once "connect.php";

$login = $_SESSION['login'];

if (isset($lang) && $lang=="C/C++")
{

}

if (isset($lang) && $lang=="C/C++")
{
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO ctopics VALUES (NULL,'$login','$message')"))
            {
                header('Location: C.php');
            }
            else
            {
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        echo $exception;
    }



}
if (isset($lang) && $lang=="Python")
{
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO pytopics VALUES (NULL,'$login','$message')"))
            {
                header('Location: Python.php');
            }
            else
            {
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        echo $exception;
    }

}
if (isset($lang) && $lang=="Java")
{
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO javatopics VALUES (NULL,'$login','$message')"))
            {
                header('Location: Java.php');
            }
            else
            {
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        echo $exception;
    }
}
if (isset($lang) && $lang=="PHP")
{
    try
    {
        $connection = new mysqli($host, $db_user, $db_password, $db_name);
        if ($connection->connect_errno!=0)
        {
            throw new Exception(mysqli_connect_errno());
        }
        else
        {
            if($connection->query("INSERT INTO phptopics VALUES (NULL,'$login','$message')"))
            {
                header('Location: PHP.php');
            }
            else
            {
                throw new Exception($connection->error);
            }
        }
    }
    catch (Exception $exception)
    {
        echo $exception;
    }

}
else
{
    echo '<span style="color:red">Language is not selected!</span>';
}
?>