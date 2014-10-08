from django.contrib import admin
from main_app.models import Remind


class RemindAdmin(admin.ModelAdmin):
    list_display = [
        'remind_date', 'remind_text',
        'remind_email', 'remind_cycle'
    ]

admin.site.register(Remind, RemindAdmin)
