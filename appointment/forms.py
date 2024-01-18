from django import forms
from .models import Appointment  

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Appointment  
        fields = '__all__'
