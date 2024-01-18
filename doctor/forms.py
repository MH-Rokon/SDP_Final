from .models import Doctor
from django import forms

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = '__all__'
       