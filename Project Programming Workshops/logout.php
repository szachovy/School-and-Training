<?php

#reset wszystkich zmiennych sesyjnych
session_start();

session_unset();


header('Location: index.php');

?>