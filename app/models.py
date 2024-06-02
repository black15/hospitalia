from django.db import models
from account.models import Doctor, Patient

class Reservation(models.Model):
    patient          = models.ForeignKey(Patient, verbose_name="Patient", on_delete=models.CASCADE, null=True)
    doctor           = models.ForeignKey(Doctor, verbose_name="Doctor", on_delete=models.CASCADE, null=True)
    reservation_date = models.DateTimeField("Reservation Date", auto_now_add=True)

    def __str__(self):
        return '{0}, {1}'.format(self.patient, self.reservation_date)
    
class DoctorRoom(models.Model):
    number = models.CharField("Room Number", max_length=50)

    def __str__(self):
        return f'room {self.number}'
    