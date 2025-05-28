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
    """Formats the subject line for an email"""
    subject = (
        'Job Digest ' + str(date.today()) + ' ' + 
        str(datetime.now().hour) + ':' + str(datetime.now().minute)
    )
    return subject

def format_email_body(job_list):
    """Formats the body for the job posting digest"""
    html = "<h2>New Job Postings</h2><ul>"
    for job in job_list:
        html += f"<li><a href='{job['url']}'>{job['title']} at {job['company']}</a><br>"
        html += f"<i>{job['location']} - Posted {job['posted_date']}</i><br>"
        html += f"{job['description_snippet']}</li><br><br>"
    html += "</ul>"
    return html

def send_email(subject, body):
    """Sends an email"""
    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    mime_html = MIMEText(body, 'html')
    msg.attach(mime_html)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(login, password)
        server.sendmail(from_email, to_email, msg.as_string())
    