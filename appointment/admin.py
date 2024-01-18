# admin.py
from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('account', 'doctor', 'appointment_status', 'symptom', 'time', 'cancel')

# Register the model with the admin site
admin.site.register(Appointment, AppointmentAdmin)
