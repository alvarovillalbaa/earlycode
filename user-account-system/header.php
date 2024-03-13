<?php
// This is an example of what php Symbol Oriented Programming can do
// We must do a testnet web design and integrate it with the login_system
// for that we need an index, a signup and a login page
session_start();
// being the header a common symbol to all pages, the user would be logged in all the websites
?>

<!-- we can include the following in the index.php(inside section and php tags):
if (isset($_SESSION['useruid'])) {
    echo '<p>Hello there ' . $_SESSION['useruid'] . '!</p>'
}
-->
<section class="whatever">
    <h2>whatever</h2>
    <!-- This header should be symbol-wise and represent the navbar -->
    <?php
    // we aim to change the web display if the user is logged in
    if (isset($_SESSION['useruid'])) {
        echo '<li><a href="profile.php">Profile</a></li>';
        echo '<li><a href="includes/logout.inc.php">Log Out</a></li>';
    } else {
        // the one to display if not logged in
        echo '<li><a href="signup.php">Sign Up</a></>';
    }
    ?>
</section>