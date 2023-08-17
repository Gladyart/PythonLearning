import ssl
import smtplib
from AppPGM import password
from email.message import EmailMessage
from getpass import getpass

emailSender = input('Login: ')
emailPassword = getpass()
emailReceiver = input('Enter receiver: ')

subject = "Test email notification"
body = """
Dear all!
Some notification sent.
"""

em = EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())
