<?php

function emptyInputSignup($name, $email, $username, $pwd, $pwdRepeat)
{
    $result; // || means OR
    if (empty($name) || empty($email) || empty($username) || empty($pwd) || empty($pwdRepeat)) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}

function invalidUid($username)
{
    $result;
    // regex with search username
    if (!preg_match('/^[a-zA-Z0-9]*$/', $username)) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}

function invalidEmail($email)
{
    $result;
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}

function pwdMatch($pwd, $pwdRepeat)
{
    $result;
    if ($pwd !== $pwdRepeat) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}

function uidExists($connection, $username)
{
    // ? is a placeholder, we do not immediately check for it
    $sql = 'SELECT * FROM users WHERE usersUid = ? OR usersEmail = ?;';
    // everything is binded to our $stmt prepared statement
    $stmt = mysqli_stmt_init($connection);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        // if there is an error
        header('location: ../signup.php?error=stmtfailed');
        exit();
    }

    // pass the data from the user
    // ss means two strings(what type of data you're passing)
    mysqli_stmt_bind_param($stmt, 'ss', $username, $email);
    mysqli_stmt_execute($stmt);

    $resultData = mysqli_stmt_get_result($stmt);

    // check if there is any data in the associative array(array with names associated to columns)
    // grab username, etc. on the login form
    // row assigns the data to the rows, created this variable while checking info
    if ($row = mysqli_fetch_assoc($resultData)) {
        return $row;
    } else {
        $result = false;
        return $result;
    }

    mysqli_stmt_close($stmt);
}

function createUser($connection, $name, $email, $username, $pwd)
{
    $sql = 'INSERT INTO users (usersName, usersEmail, usersUid, usersPwd) VALUES (?, ?, ?, ?)';
    $stmt = mysqli_stmt_init($connection);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header('location: ../signup.php?error=stmtfailed');
        exit();
    }

    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);

    // we have four strings of data
    mysqli_stmt_bind_param($stmt, 'ssss', $name, $email, $username, $hashedPwd);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    // sending the user to a location after signing up successfully
    header('location: ../signup.php?error=none');
    exit();
}

function emptyInputLogin($username, $pwd)
{
    $result; // || means OR
    if (empty($username) || empty($pwd)) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}

function loginUser($connection, $username, $pwd)
{
    // double $username but has to return a true from line 51, either usersUid or usersEmail
    $uidExists = uidExists($connection, $username, $username);

    if ($uidExists === false) {
        header('location: ../login.php?error=wronglogin');
        exit();
    }

    // as an associative array, we check by column names
    $pwdHashed = $uidExists['usersPwd'];
    $checkPwd = password_verify($pwd, $pwdHashed);

    if ($checkPwd === true) {
        // we need to start the session first
        session_start();
        $_SESSION['userid'] = $uidExists['usersId'];
        $_SESSION['useruid'] = $uidExists['usersUid'];
        header('location: ../index.php');
        exit();
    }
}
