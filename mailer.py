from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate
import smtplib
from threading import Thread
import logging
from main.settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


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
    mail['From'] = EMAIL_HOST_USER
    mail['To'] = ';'.join(email_addresses)
    mail['Date'] = formatdate()

    try:
        smtp = smtplib.SMTP_SSL(EMAIL_HOST, smtplib.SMTP_SSL_PORT)
        smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

        smtp.sendmail(EMAIL_HOST_USER, email_addresses, mail.as_string())
        smtp.close()
        logging.info('email sended successfully')
    except Exception as e:
        logging.error(str(e))


def send_email(email_addresses, subject, content):
    Thread(target=_send_email,
           args=[email_addresses, subject, content]).start()
