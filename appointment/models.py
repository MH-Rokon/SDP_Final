from django.db import models
from django.contrib.auth.models import User  
from accounts.models import UserMaxAccount
from doctor.models import Doctor, AvailableTime

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]



class Appointment(models.Model):
    account = models.ForeignKey(UserMaxAccount, related_name='appointments', on_delete=models.CASCADE, default=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS, max_length=10, default="Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)  # Ensure this is correct based on your AvailableTime model
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name}, Patient: {self.account.user.first_name}"
