# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Remind(models.Model):
    class Meta:
        verbose_name_plural = '我的提醒'

    remind_date = models.DateTimeField('提醒日期')
    remind_text = models.CharField('提醒信息', max_length=128)
    remind_email = models.EmailField('提醒邮箱')
    remind_cycle = models.CharField(
        '提醒周期',
        max_length=10,
        choices=(
            ('everyyear', '每年'),
            ('everymonth', '每月'),
            ('everyweek', '每周'),
            ('everyday', '每天'),
            ('once', '仅一次'),
        ),
        default='everyyear'
    )

    def __str__(self):
        return datetime.strftime(self.remind_date, '%m-%d %H:%M:%S')
