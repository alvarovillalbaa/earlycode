from email import message
import smtplib
import ssl  # To access the mail server(secure socket layer)
from email.message import EmailMessage

subject = "Email Automation"
body = "This is a test email from Python!"
sender_email = "alvaro.villalbaperez@gmail.com"
receiver_email = "alvaro.villalbaperez@gmail.com"
password = input("Enter a password:")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = (
    ssl.create_default_context()
)  # To overcome mail cyberseurity as we don't have our own server

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    # 465 is the port connection
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
