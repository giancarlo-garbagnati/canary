"""for sending emails"""

from datetime import date, datetime
from config import email_config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from_email = email_config.EMAIL_FROM
to_email = email_config.EMAIL_TO
smtp_server = email_config.SMTP_SERVER
smtp_port = email_config.SMTP_PORT
login = email_config.EMAIL_USER
password = email_config.EMAIL_PASS


def format_email_subject():
    subject = (
        'Job Digest ' + str(date.today()) + ' ' + 
        str(datetime.now().hour) + ':' + str(datetime.now().minute)
    )
    return subject

def format_email_body():
    pass

def send_email(subject, body):
    pass