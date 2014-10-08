from django.contrib import admin
from app.models import Remind

class RemindAdmin(admin.ModelAdmin):
    fields = ['remind_date', 'remind_text', 'remind_email', 'remind_cycle']

admin.site.register(Remind, RemindAdmin)
