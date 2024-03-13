<?php
// Inserting a hyperlink to optimise website performance
include_once 'header.php';
?>

<section class='signup-form'>
    <h2>Log In</h2>
    <form action='includes/login.inc.php' method='post'>
        <!-- .inc. is included when it is a simple php script running on the server side-->
        <input type='text' name='uid' placeholder='Username/Email...'>
        <input type='password' name='pwd' placeholder='Password...'>
        <button type='submit' name='submit'>Log In</button>
    </form>
    <?php
    if (isset($_GET['error'])) {
        if ($_GET['error'] == 'emptyinput') {
            echo '<p>Fill in all the fields, please!</p>';
        } else if ($_GET['error'] == 'wronglogin') {
            echo '<p>Incorrect credentials!</p>';
        }
    }
    ?>
</section>