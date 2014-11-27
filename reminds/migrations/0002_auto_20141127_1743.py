# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reminds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remind',
            name='remind_cycle',
            field=models.CharField(default='yearly', max_length=10, verbose_name='\u63d0\u9192\u5468\u671f', choices=[('yearly', '\u6bcf\u5e74'), ('monthly', '\u6bcf\u6708'), ('weekly', '\u6bcf\u5468'), ('daily', '\u6bcf\u5929'), ('once', '\u4ec5\u4e00\u6b21')]),
        ),
        migrations.AlterField(
            model_name='remind',
            name='remind_date',
            field=models.DateTimeField(verbose_name='\u63d0\u9192\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='remind',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
