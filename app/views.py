from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Account, Doctor, Patient
from .models import Reservation, DoctorRoom
from .forms import ReservationForm

def home(request):
    context = {}

    if request.user.is_authenticated:
        
        doctors = Doctor.objects.all()

        if request.user.is_patient:
            context['patient'] = Patient.objects.get(user=request.user)
            context['usertype'] = 'patient'

            patient=Patient.objects.get(user=request.user)
            
            if Reservation.objects.filter(patient=patient):
                _res = Reservation.objects.order_by('reservation_date')
    
                # Initialize position variables
                position = None
                patients_in_front = None
                
                # Loop through the ordered reservations and determine the position of the logged-in patient
                for index, reservation in enumerate(_res):
                    if reservation.patient == patient:
                        position = index + 1
                        patients_in_front = index
                        break
                    
                context['pos']          = position
                context['infront']      = patients_in_front
                context['patient_has']  = True
                context['reservation']  = Reservation.objects.get(patient=patient)

            else:
                context['patient_has'] = False
                if request.method == 'POST':
                    if request.POST.get('doctor'):
                        doctor = Doctor.objects.get(full_name=request.POST.get('doctor'))
                        patient = Patient.objects.get(user=request.user)
                        reservation = Reservation.objects.create(patient=patient, doctor=doctor)
                        return redirect('app:home')
        
        elif request.user.is_doctor:
            rooms       = DoctorRoom.objects.all()
            doctor = Doctor.objects.get(user=request.user)
            _res   = Reservation.objects.filter(doctor=doctor).count()
            f_res  = Reservation.objects.filter(doctor=doctor).first()

            context['usertype'] = 'doctor'
            context['doctor']   = doctor
            context['first']    = f_res
            context['count']    = _res
            context['rooms']    = rooms


    if not request.user.is_authenticated:
        return redirect('account:home')
        
    context['doctors'] = doctors
    context['form'] = ReservationForm()
    return render(request, 'app/home.html', context)

def call_patient(request, res_id):
    # Fetch the reservation instance
    if request.method == 'POST':
        
        reservation = Reservation.objects.get(id=res_id)
        print(reservation.doctor.service)
        # Delete the reservation
        reservation.delete()
        
        # Display a success message
        messages.success(request, f'Patient {reservation.patient.full_name} has been called to room number {request.POST.get('room')}.')
        
    return redirect('app:home')