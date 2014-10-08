# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remind_date', models.DateTimeField(verbose_name=b'Remind Date')),
                ('remind_text', models.CharField(max_length=128, verbose_name=b'Remind Text')),
                ('remind_email', models.EmailField(max_length=75, verbose_name=b'Remind Email')),
                ('remind_cycle', models.CharField(default=b'everyyear', max_length=10, verbose_name=b'Remind Cycle', choices=[(b'everyyear', b'everyyear'), (b'everymonth', b'everymonth'), (b'everyweek', b'everyweek'), (b'everyday', b'everyday'), (b'once', b'once')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
