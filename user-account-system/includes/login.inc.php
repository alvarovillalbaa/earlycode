<?php

if (isset($_POST['submit'])) {
    // it is originally Userrname or Email, but do not worry
    $username = $_POST['uid'];
    $pwd = $_POST['pwd'];

    require_once 'dbh.inc.php';
    require_once 'functions.inc.php';

    if (emptyInputLogin($username, $pwd) !== false) {
        header('location: ../login.php?error=emptyinput');
        exit();
    }

    loginUser($connection, $username, $pwd);
} else {
    header('location: ../login.php');
    exit();
}
