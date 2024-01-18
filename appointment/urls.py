from django.urls import path
from appointment.views import BookAppointment
from . import views

urlpatterns = [
    # path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path('book_appointment/<int:doctor_id>/', BookAppointment, name='book_appointment'),
]
