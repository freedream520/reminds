from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate
import smtplib
from threading import Thread
import os
from decouple import config

MAIL_HOST = config('MAIL_HOST')
MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')

def _to_list(emails):
    if isinstance(emails, basestring):
        emails = [emails]
    return emails


def _send_email(email_addresses, subject, content):
    email_addresses = _to_list(email_addresses)

    mail = MIMEText(
        content,
        _subtype="html",
        _charset="utf-8"
    )
    mail['Subject'] = Header(subject, 'utf-8')
    mail['From'] = MAIL_USERNAME
    mail['To'] = ';'.join(email_addresses)
    mail['Date'] = formatdate()

    try:
        smtp = smtplib.SMTP_SSL(MAIL_HOST, smtplib.SMTP_SSL_PORT)
        smtp.login(MAIL_USERNAME, MAIL_PASSWORD)

        smtp.sendmail(MAIL_USERNAME, email_addresses, mail.as_string())
        smtp.close()
    except Exception as e:
        print e


def send_email(email_addresses, subject, content):
    Thread(target=_send_email,
           args=[email_addresses, subject, content]).start()
