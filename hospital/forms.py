from django import forms
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['disease_nm','p_name', 'p_phone_no', 'p_address', 'dob', 'blood_group', 'appoint_datetime']

