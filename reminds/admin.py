# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from reminds.models import Remind
from datetime import datetime
import fileinput
import os
import sys

def delete_selected(modeladmin, request, queryset):
    ids = []
    for i in queryset:
        ids.append(i.id)
        i.delete()
    for line in fileinput.input('remind.cron', inplace=True):
        remind_id = line.split('#')[1]
        if remind_id in ids:
            line = ''
        sys.stdout.write(line)
    os.system('crontab remind.cron')
delete_selected.short_description = '删除已选项'

def remind_date(obj):
    return datetime.strftime(obj.remind_date, '%m-%d %H:%M:%S')
remind_date.short_description = '提醒日期'


class RemindAdmin(admin.ModelAdmin):
    list_display = [
        remind_date, 'remind_text',
        'remind_email', 'remind_cycle', 'user'
    ]

    search_fields = ['remind_text']
    list_filter = ['remind_date']

    actions = [delete_selected]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        if not request.user.is_superuser:
            return super(RemindAdmin, self).get_queryset(request).filter(user=request.user)
        else:
            return super(RemindAdmin, self).get_queryset(request).all()


admin.site.register(Remind, RemindAdmin)
