<?php
include_once 'includes/dbh.inc.php';
// We can create different types of accounts with different permissions
// throughout the platform by declaring another numeric variable representing
// the type of user and assigning its values manually
// also, the admin can have access to assigning values from the platform
// using forms and etc
?>
<!DOCTYPE html>
<html>

<head>
    <title></title>
</head>

<body>

    <!-- This is a form where data from the web is inserted into the database-->
    <form action='includes/web_to_ddbb.inc.php' method='POST'>
        <input type='text' name='name' placeholder='Full Name'>
        <input type='text' name='email' placeholder='Enter your Email'>
        <input type='text' name='uid' placeholder='Username'>
        <input type='password' name='pwd' placeholder='Password'>
        <button type='submit' name='submit'>Sign Up</button>
    </form>

    <?php
    $sql = 'SELECT * FROM users;';
    // calling the code, sending it to the ddbb and running it on the server
    $result = mysqli_query($connection, $sql);
    // to check if there's any result
    $resultCheck = mysqli_num_rows($result);
    // to get an output only when there's a result
    if ($resultCheck > 0) {
        // creating a variable inside the while function which goes through the rows
        while ($row = mysqli_fetch_assoc($result)) {
            echo $row['usersUid'] . '<br>';
        }
    }
    ?>
</body>

</html>