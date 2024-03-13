<?php

session_start();

if (isset($_POST['submtLogin'])) {
    $_SESSION['user'] = 1;
    header('Location: index.php');
}
