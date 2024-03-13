<?php
// connecting the ddbb
include_once 'dbh.inc.php';

// mysqli_real_escape_string is a helping function to avoid SQL injection attacks
// connecting the form inputs to variables in the database
$name = mysqli_real_escape_string($connection, $_POST['name']);
$email = mysqli_real_escape_string($connection, $_POST['email']);
$uid = mysqli_real_escape_string($connection, $_POST['uid']);
$pwd = mysqli_real_escape_string($connection, $_POST['pwd']);

$sql = "INSERT INTO users
(usersName, usersEmail, usersUid, usersPwd)
VALUES
('$name', '$email', '$uid', '$pwd');";
mysqli_query($connection, $sql);

header('location: ../index.php?signup=success');
