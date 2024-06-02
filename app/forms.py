from django import forms
from .models import Reservation
from account.models import Doctor

class ReservationForm(forms.ModelForm):
    
    # listOfServices = list(Doctor.objects.all().values_list('service', flat=True))
    # service = forms.ChoiceField(choices=listOfServices, required=False)
    
    class Meta:
        model = Reservation
        fields = ['patient', 'doctor',]
