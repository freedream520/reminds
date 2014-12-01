# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
import sys
import fileinput
import threading


BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
cmd = u'%s/venv/bin/python %s/send_remind.py >/dev/null 2>&1' % (BASE_DIR, BASE_DIR)
cron_file = os.path.join(BASE_DIR, 'remind.cron')

if not os.path.exists(cron_file):
    os.system('touch %s' % cron_file)

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
        cron = self.parse_cron(self.remind_date, self.remind_cycle)
        threading.Thread(target=self.update_cron, args=[cron]).start()

    def delete(self):
        rid = '#%s' % self.id
        threading.Thread(target=self.remove_cron, args=[rid]).start()
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
        for line in fileinput.input(cron_file, inplace=True):
            if 'r_id%s' % self.id in line:
                line = cron + '\n'
                is_update = True
            sys.stdout.write(line.encode('utf-8'))
        if not is_update:
            with open(cron_file, 'a+') as crontab:
                crontab.write(cron.encode('utf-8') + '\n')
        os.system('crontab %s' % cron_file)

    def remove_cron(self, remind_id):
        for line in fileinput.input(cron_file, inplace=True):
            if remind_id in line:
                line = ''
            sys.stdout.write(line.encode('utf-8'))
        os.system('crontab %s' % cron_file)
