<?php
// Inserting a hyperlink to optimise website performance
include_once 'header.php';
// index.html > *.html > index.php > *.php
?>

<section class='signup-form'>
    <h2>Sign Up</h2>
    <form action='includes/signup.inc.php' method='post'>
        <!-- .inc. is included when it is a simple php script running on the server side-->
        <input type='text' name='name' placeholder='Full Name...'>
        <input type='text' name='email' placeholder='Email...'>
        <input type='text' name='uid' placeholder='Username...'>
        <input type='password' name='pwd' placeholder='Password...'>
        <input type='password' name='pwdconfirm' placeholder='Repeat Password...'>
        <button type='submit' name='submit'>Sign Up</button>

    </form>
    <?php
    // with $_GET we check for data in the url that  we can see(when there is ?error=...), $_POST checks for data we cannot see
    if (isset($_GET['error'])) {
        // == to what is after ?error= in the url, which we have declared in the signup.inc.php
        if ($_GET['error'] == 'emptyinput') {
            echo '<p>Fill in all the fields, please!</p>';
        } else if ($_GET['error'] == 'invaliduid') {
            echo '<p>Choose a valid username!</p>';
        } else if ($_GET['error'] == 'invalidemail') {
            echo '<p>Choose a valid email!</p>';
        } else if ($_GET['error'] == 'passwordsdontmatch') {
            echo '<p>Passwords do not match! Try again.</p>';
        } else if ($_GET['error'] == 'stmtfailed') {
            echo '<p>Something went wrong, try again!</p>';
        } else if ($_GET['error'] == 'usernametaken') {
            echo '<p>This username is already taken!</p>';
        } else if ($_GET['error'] == 'none') {
            echo '<p>You have already signed up!</p>';
        }
    }
    ?>
</section>