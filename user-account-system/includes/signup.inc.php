<?php

// if this is set inside, go, if not, get out
if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $username = $_POST['uid'];
    $pwd = $_POST['pwd'];
    $pwdRepeat = $_POST['pwdrepeat'];

    // connecting to the database
    require_once 'dbh.inc.php';
    require_once 'functions.inc.php';

    if (emptyInputSignup($name, $email, $username, $pwd, $pwdRepeat) !== false) {
        // !== false instead of === true to throw an error correctly
        header('location: ../signup.php?error=emptyinput');
        exit();
    }
    if (invalidUid($username) !== false) {
        header('location: ../signup.php?error=invaliduid');
        exit();
    }
    if (invalidEmail($email) !== false) {
        header('location: ../signup.php?error=invalidemail');
        exit();
    }
    if (pwdMatch($pwd, $pwdRepeat) !== false) {
        header('location: ../signup.php?error=passwordsdontmatch');
    }
    if (uidExists($connection, $username) !== false) {
        header('location: ../signup.php?error=usernametaken');
    }

    createUser($connection, $name, $email, $username, $pwd);
} else {
    header('location: ../signup.php');
    exit();
}
