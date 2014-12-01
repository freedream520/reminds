# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
import sys
import fileinput


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
cmd = u'%s/.venv/bin/python %s/send_remind.py' % (BASE_DIR, BASE_DIR)

class Remind(models.Model):

    class Meta:
        verbose_name_plural = u'我的提醒'

    user = models.ForeignKey(User, verbose_name=u'用户名', editable=False, null=True, blank=True)
    remind_date = models.DateTimeField(u'提醒时间')
    remind_text = models.CharField(u'提醒信息', max_length=128)
    remind_email = models.EmailField(u'提醒邮箱')
    remind_cycle = models.CharField(
        u'提醒周期',
        max_length=10,
        choices=(
            ('yearly', u'每年'),
            ('monthly', u'每月'),
            ('weekly', u'每周'),
            ('daily', u'每天'),
            ('once', u'仅一次'),
        ),
        default='yearly'
    )

    def __str__(self):
        return datetime.strftime(self.remind_date, '%m-%d')

    def save(self, *args, **kwargs):
        super(Remind, self).save(*args, **kwargs)
        self.update_cron(self.parse_cron(
            self.remind_date, self.remind_cycle))

    def delete(self):
        self.remove_cron('#%s' % self.id)
        super(Remind, self).delete()

    def parse_cron(self, date, cycle):
        if cycle == 'once':
            cron = u'%s %s %s %s %s %s %s %s r_id%s' % (
                date.minute, date.hour, date.day,
                date.month, date.isoweekday(), cmd,
                self.remind_email, self.remind_text, self.id)
        elif cycle == 'daily':
            cron = u'%s %s * * * %s %s %s r_id%s' % (
                date.minute, date.hour, cmd,
                self.remind_email, self.remind_text, self.id)
        elif cycle == 'weekly':
            cron = u'%s %s * * %s %s %s %s r_id%s' % (
                date.minute, date.hour, date.isoweekday(), cmd,
                self.remind_email, self.remind_text, self.id)
        elif cycle == 'monthly':
            cron = u'%s %s %s * * %s %s %s r_id%s' % (
                date.minute, date.hour, date.day, cmd,
                self.remind_email, self.remind_text, self.id)
        elif cycle == 'yearly':
            cron = u'%s %s %s %s * %s %s %s r_id%s' % (
                date.minute, date.hour, date.day, date.month, cmd,
                self.remind_email, self.remind_text, self.id)
        return cron

    def update_cron(self, cron):
        is_update = False
        for line in fileinput.input('remind.cron', inplace=True):
            if 'r_id%s' % self.id in line:
                line = cron + '\n'
                is_update = True
            sys.stdout.write(line)
        if not is_update:
            with open('remind.cron', 'a+') as crontab:
                crontab.write(cron.encode('utf-8') + '\n')
        os.system('crontab remind.cron')

    def remove_cron(self, remind_id):
        for line in fileinput.input('remind.cron', inplace=True):
            if remind_id in line:
                line = ''
            sys.stdout.write(line)
        os.system('crontab remind.cron')
