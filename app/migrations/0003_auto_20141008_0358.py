# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141008_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remind',
            name='remind_text',
            field=models.CharField(max_length=128, verbose_name=b'Remind Text'),
        ),
    ]
