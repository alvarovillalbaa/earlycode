<?php
// dbh stands for database handler, the one connected to the database
// if we leave empty lines, it could through an error on the server
// to avoid that, we can leave it open
$serverName = 'localhost';
$dBUsername = 'root';
$dBPassword = '';
$dBName = 'login_system';

// PDO stands for PHP Data Objects
// mySQLi is secure, mySQL is not anymore
$connection = mysqli_connect($serverName, $dBUsername, $dBPassword, $dBName);

// to throw error if connection fails(if $connection throws False)
if (!$connection) {
    die('Connection failed: ' . mysqli_connect_error());
}
