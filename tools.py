#-*- coding:utf-8 -*-
import hashlib
import random
import re

def get_email_url(email):
    return re.sub('.+@', 'mail.', email)

def get_reset_password_code(user):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    return hashlib.sha1(salt + user.username.encode('utf-8')).hexdigest()

def clearup_text(text):
    text = text.replace('"', "'")
    return '"%s"' % text
