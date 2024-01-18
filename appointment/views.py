from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView
from appointment.constants import Patient_Appointment
from datetime import datetime
from django.db.models import Sum
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from appointment.forms import TransactionForm
from doctor.models import Doctor, Profile, AvailableTime
from appointment.models import Appointment

# Function to send transaction email
def send_transaction_email(user, time_slot, subject, template):
    message = render_to_string(template, {
        'user': user,
        'time_slot': time_slot,
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

def BookAppointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    # Assuming doctor has an available_time field representing available time slots
    available_times = doctor.available_time.all()

    if available_times.exists():
        # Choose an available time (you may need to adjust this logic based on your requirements)
        selected_time = available_times.first()

        # Create the appointment with the selected time
        appointment = Appointment.objects.create(
            account=request.user.account,
            doctor=doctor,
            appointment_status='Pending',
            time=selected_time,  # Provide a value for the time field
            # Adjust accordingly based on your model
        )

        # Add the doctor to the user's saved appointments
        user_profile.saved_appointment.add(doctor)

        messages.success(
            request,
            f'Successfully booked the appointment with Dr. {doctor.name}.'
        )

        send_transaction_email(
            request.user,
            appointment.time,  # You may need to adjust this based on your model
            "Book Appointment Message",
            "appointment/bookappointment_email.html"
        )
    else:
        messages.error(
            request,
            f'Sorry, no available time slots for Dr. {doctor.name}.'
        )

    return redirect('profile')
