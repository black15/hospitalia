from django.urls import path
from .views import *

app_name= 'account'

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('register/patient/', patient_register, name='patient_register'),
    path('register/doctor/', doctor_register, name='doctor_register'),
]
