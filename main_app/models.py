from django.db import models
from datetime import datetime


class Remind(models.Model):
    remind_date = models.DateTimeField('Remind Date')
    remind_text = models.CharField('Remind Text', max_length=128)
    remind_email = models.EmailField('Remind Email')
    remind_cycle = models.CharField(
        'Remind Cycle',
        max_length=10,
        choices=(
            ('everyyear', 'everyyear'),
            ('everymonth', 'everymonth'),
            ('everyweek', 'everyweek'),
            ('everyday', 'everyday'),
            ('once', 'once'),
        ),
        default='everyyear'
    )

    def __str__(self):
        return datetime.strftime(self.remind_date, '%m-%d %H:%M:%S')
