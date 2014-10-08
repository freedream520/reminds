# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Remind(models.Model):
    class Meta:
        verbose_name_plural = '我的提醒'

    user = models.ForeignKey(User, editable=False, null=True, blank=True)
    remind_date = models.DateTimeField('提醒日期')
    remind_text = models.CharField('提醒信息', max_length=128)
    remind_email = models.EmailField('提醒邮箱')
    remind_cycle = models.CharField(
        '提醒周期',
        max_length=10,
        choices=(
            ('year', '每年'),
            ('month', '每月'),
            ('week', '每周'),
            ('day', '每天'),
            ('once', '仅一次'),
        ),
        default='year'
    )

    def __str__(self):
        return datetime.strftime(self.remind_date, '%m-%d %H:%M:%S')
