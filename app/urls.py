from django.urls import path
from .views import home, call_patient

app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('call/<int:res_id>/', call_patient, name='call_patient'),
]
