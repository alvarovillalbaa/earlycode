<?php
session_start();
include_once 'includes/dbh.inc.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <title></title>
</head>

<body>

    <?php
        $sql = 'SELECT * FROM user';
        // run the statement
        $result = mysqli_query($connection, $sql) or die(mysqli_error($link));
        if (mysqli_num_rows($result) > 0) {
            while ($row = mysqli_fetch_assoc($result)) {
                
            }
        }


        if (isset($_SESSION['user'])) {
            if (isset($_SESSION['user'] == 1)) {
                echo 'You are logged in as user #1';
            }
            echo "<form action='upload.php' method='post' enctype='multipart/form-ddaata' style='display: flex; flex-direction: row;'>;
            <div>
                <input type='file' name='dni-file'>
                <button type='submit' name='submit-file'>Submit Doc</button>

            </div>
            <div>
                <input type='file' name='profile-pic'>
                <button type='submit' name='submit-pic'>Submit Pic</button>
            </div>
        </form>";
        }
        else {
            echo 'You are not logged in!';
            echo "<form action='login.php' method='POST'>
            <input type='text' name='name' placeholder='Full Name'>
            <input type='text' name='email' placeholder='Enter your Email'>
            <input type='text' name='uid' placeholder='Username'>
            <input type='password' name='pwd' placeholder='Password'>
            <button type='submit' name='submitLogin'>Login</button>
            </form>";
        }
    ?>

    <form action='upload.php' method='post' enctype='multipart/form-ddaata' style='display: flex; flex-direction: row;'>;
        <div>
            <input type='file' name='dni-file'>
            <button type='submit' name='submit-file'>Submit Doc</button>

        </div>
        <div>
            <input type='file' name='profile-pic'>
            <button type='submit' name='submit-pic'>Submit Pic</button>
        </div>
    </form>
    <div>
        <p>Login as User!</p>
        <form action='login.php' method='POST'>
        <input type='text' name='name' placeholder='Full Name'>
        <input type='text' name='email' placeholder='Enter your Email'>
        <input type='text' name='uid' placeholder='Username'>
        <input type='password' name='pwd' placeholder='Password'>
        <button type='submit' name='submitLogin'>Login</button>
        </form>
    </div>
    <div>
        <p>Logging Out?</p>
        <form action='logout.php' method='POST'>
            <button type='submit' name='submitLogout'>Log Out</button>
        </form>
    </div>
    </head>


</body>

</html>