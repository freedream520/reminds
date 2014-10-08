# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Remind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remind_date', models.DateTimeField(verbose_name='\u63d0\u9192\u65e5\u671f')),
                ('remind_text', models.CharField(max_length=128, verbose_name='\u63d0\u9192\u4fe1\u606f')),
                ('remind_email', models.EmailField(max_length=75, verbose_name='\u63d0\u9192\u90ae\u7bb1')),
                ('remind_cycle', models.CharField(default='year', max_length=10, verbose_name='\u63d0\u9192\u5468\u671f', choices=[('year', '\u6bcf\u5e74'), ('month', '\u6bcf\u6708'), ('week', '\u6bcf\u5468'), ('day', '\u6bcf\u5929'), ('once', '\u4ec5\u4e00\u6b21')])),
                ('user', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': '\u6211\u7684\u63d0\u9192',
            },
            bases=(models.Model,),
        ),
    ]
