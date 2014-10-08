# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remind',
            name='remind_cycle',
            field=models.CharField(default=b'everyyear', max_length=10, verbose_name=b'Remind Cycle', choices=[(b'everyyear', b'everyyear'), (b'everymonth', b'everymonth'), (b'everyweek', b'everyweek'), (b'everyday', b'everyday'), (b'once', b'once')]),
        ),
        migrations.AlterField(
            model_name='remind',
            name='remind_email',
            field=models.EmailField(max_length=75, verbose_name=b'Remind Email'),
        ),
        migrations.AlterField(
            model_name='remind',
            name='remind_text',
            field=models.TextField(verbose_name=b'Remind Text'),
        ),
    ]
