# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
import sys
import fileinput


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
            ('yearly', '每年'),
            ('monthly', '每月'),
            ('weekly', '每周'),
            ('daily', '每天'),
            ('once', '仅一次'),
        ),
        default='yearly'
    )

    def __str__(self):
        return datetime.strftime(self.remind_date, '%m-%d %H:%M')

    def save(self, *args, **kwargs):
        super(Remind, self).save(*args, **kwargs)
        self.update_cron(self.parse_cron(
            self.remind_date, self.remind_cycle))

    def parse_cron(self, date, cycle):
        if cycle == 'once':
            cron = '%s %s %s %s %s send_remind #%s' % (
                date.minute, date.hour, date.day, date.month, date.isoweekday(), self.id)
        elif cycle == 'daily':
            cron = '%s %s * * * send_remind #%s' % (
                date.minute, date.hour, self.id)
        elif cycle == 'weekly':
            cron = '%s %s * * %s send_remind #%s' % (
                date.minute, date.hour, date.isoweekday(), self.id)
        elif cycle == 'monthly':
            cron = '%s %s %s * * send_remind #%s' % (
                date.minute, date.hour, date.day, self.id)
        elif cycle == 'yearly':
            cron = '%s %s %s %s * send_remind #%s' % (
                date.minute, date.hour, date.day, date.month, self.id)
        return cron

    def update_cron(self, cron):
        remind_id = '#' + cron.split('#')[1]
        is_update = False
        for line in fileinput.input('remind.cron', inplace=True):
            if remind_id in line:
                line = cron + '\n'
                is_update = True
            sys.stdout.write(line)
        if not is_update:
            with open('remind.cron', 'a+') as crontab:
                crontab.write(cron + '\n')
        os.system('crontab remind.cron')

    def remove_cron(self, cron):
        pass
