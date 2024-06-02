from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class PatientLoginForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Username'}))
    password    = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Password'}))

class PatientCreationForm(UserCreationForm):
    
    full_name       = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Patient name'}))
    phone_number    = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Phone Number'}))
    username    = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Username'}))
    password1    = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Password'}))
    passcat    = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Password Confirmation'}))
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'full_name', 'phone_number', 'password1', 'passcat']
        
    def __init__(self, *args, **kwargs):
        super(PatientCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

    @transaction.atomic
    def save(self):
        print(self.cleaned_data['full_name'])
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        Patient.objects.create(user=user, full_name=self.cleaned_data['full_name'], phone_number=self.cleaned_data['phone_number'], passcat=self.cleaned_data['passcat'])
        return user

class DoctorCreationForm(UserCreationForm):

    full_name       = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Full name'}))
    phone_number    = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Phone Number'}))
    service         = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Service'}))
    username    = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Username'}))
    password1    = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Password'}))
    passcat    = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm text-gray-800 focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Password Confirmation'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'full_name', 'phone_number', 'service', 'password1', 'passcat']

    def __init__(self, *args, **kwargs):
        super(DoctorCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            Doctor.objects.create(user=user, full_name=self.cleaned_data['full_name'], phone_number=self.cleaned_data['phone_number'], service=self.cleaned_data['service'], passcat=self.cleaned_data['passcat'], )

        return user