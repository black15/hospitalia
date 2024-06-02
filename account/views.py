from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import PatientCreationForm, DoctorCreationForm, PatientLoginForm
from .models import *

# Create your views here.

def home(request):
    return render(request, 'account/whoareyou.html')

def user_login(request):
    context = {}

    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)   
                return redirect('app:home')
    else:
        form = PatientLoginForm()

    context['form'] = form
    return render(request, 'account/patient_login.html', context)

def patient_register(request):
    context = {}
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        form = PatientCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                return redirect('/')
        else: print(form.error_messages)
            
    else:
        form = PatientCreationForm()  

    context['form'] = form
    context['usertype'] = 'patient'  
    return render(request, 'account/patient_register.html', context)

def doctor_register(request):
    context = {}
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                return redirect('/')
        else: print(form.error_messages)
            
    else:
        form = DoctorCreationForm()

    context['form'] = form
    context['usertype'] = 'doctor'
    return render(request, 'account/patient_register.html', context)

def user_logout(request):
    logout(request)
    return redirect('app:home')