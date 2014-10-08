from django.db import models


class Remind(models.Model):
    remind_date = models.DateTimeField('Remind Date')
    remind_text = models.TextField()
    remind_email = models.EmailField()
    remind_cycle = models.CharField(
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
