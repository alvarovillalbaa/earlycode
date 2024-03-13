<?php
if (isset($_POST['submit'])) {
    $file = $_FILES['dni-file'];

    $fileName = $_FILES['dni-file']['name'];
    $fileTmpName = $_FILES['dni-file']['tmp-name']; // The temporary location
    $fileSize = $_FILES['dni-file']['size'];
    $fileError = $_FILES['dni-file']['error'];
    $fileType = $_FILES['dni-file']['type'];

    $fileExtension = explode('.', $fileName);
    $fileActualExtension = strtolower(end($fileExtension)); // To parametrize the data to general ISO CS

    $fileAllowed = array('jpg', 'jpeg', 'png', 'pdf');

    if (in_array($fileActualExtension, $fileAllowed)) {
        if ($fileError !== 0) {
            echo 'There was an error uploading your file';
        } else {
            if ($fileSize < 1000000) {
                $fileNewName = uniqid('', true) . '.' . $fileActualExtension;
                $fileDestination = 'profile-uploads' . $fileNewName;
                move_uploaded_file($fileTmpName, $fileDestination);
                header('Location: index.php?uploadsuccess'),
            } else {
                echo 'Your file was too big';
            }
        }
    } else {
        echo 'This file type is not allowed';
    }
}
