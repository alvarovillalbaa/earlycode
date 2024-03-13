<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Contact Form Webtest</title>
</head>


<body>
    <main>
        <p>SEND AUTOMATIC EMAIL</p>
        <form class='contact-form' method="post" action='contactform.php'>
            <input type='text' name='name' placeholder='Full Name'>
            <input type='text' name='mail' placeholder='Your Email'>
            <input type='text' name='ticket' placeholder='Subject'>
            <textarea name='message' placeholder='Your Message'></textarea>
            <button type='submit' name='name'>SEND EMAIL</button>
        </form>
    </main>