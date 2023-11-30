import smtplib
from email.message import EmailMessage
from ..venv import credentials 

def send_email(message_text, recipient_email):


    msg = EmailMessage()

    msg['Subject'] = "Empréstimo de Livro"
    msg['From'] = credentials.EMAIL
    msg['To'] = recipient_email

    msg.set_content(message_text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(credentials.EMAIL, credentials.PASSWORD)
        smtp.send_message(msg)        