# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from reminds.models import Remind
from datetime import datetime

def remind_date(obj):
    return datetime.strftime(obj.remind_date, '%m-%d %H:%M:%S')
remind_date.short_description = '提醒日期'

class RemindAdmin(admin.ModelAdmin):
    list_display = [
        remind_date, 'remind_text',
        'remind_email', 'remind_cycle'
    ]

admin.site.register(Remind, RemindAdmin)
