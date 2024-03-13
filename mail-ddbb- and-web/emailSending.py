from email import message
import email
import smtplib
import ssl
from email.message import EmailMessage
import sys

subject = ""
greeting = ""
body = ""
sender_email = "hello@orygen.earth"
receiver_email = ""
password = "password.env"
footer = "genSignature.html"

# db variables retrieving
emailType = sys.argv[1]

# we might only need to retrieve emailAddress value...
# or also the name for the greeting referred

if emailType == 1:
    # no need for loop, cause state already changed to SENT in php loop. We may need to set init value.
    subject = "/Newsletter/newsSubject"
    greeting = "/Newsletter/newsGreeting"
    body = "/Newsletter/newsBody"
elif emailType == 2:
    subject = "/Contact/contactSubject"
    greeting = "/Contact/contactGreeting"
    body = "/Contact/contactBody"
elif emailType == 3:
    subject = "/Waitlist/waitlistSubject"
    greeting = "/Waitlist/waitlistGreeting"
    body = "/Waitlist/waitlistBody"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h4>{greeting}</h4>
        <p>{body}</p>
        <footer>{footer}</footer>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string(html))
