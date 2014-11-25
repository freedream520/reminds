#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class ResetPasswordCode(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户名')
    reset_password_code = models.CharField(max_length=40, null=True, blank=True, verbose_name=u'重置码')
    reset_expires = models.DateTimeField(null=True, blank=True, verbose_name=u'重置期限')
