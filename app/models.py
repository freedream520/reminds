from django.db import models


class Remind(models.Model):
    remind_date = models.DateTimeField('Remind Date')
    remind_text = models.TextField('Remind Text')
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
