from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    is_patient  = models.BooleanField(default=False)
    is_doctor   = models.BooleanField(default=False)

class Patient(models.Model):
  user = models.ForeignKey("Account", related_name='patients', verbose_name="User", on_delete=models.CASCADE)
  full_name = models.CharField("Full name", max_length=50)
  phone_number = models.CharField("Phone number", max_length=50)
  passcat = models.CharField("Password", max_length=50, default='patient123')

  def __str__(self):
      return self.full_name
  

class Doctor(models.Model):
  user = models.ForeignKey("Account", related_name='doctors', verbose_name="User", on_delete=models.CASCADE)
  full_name = models.CharField("Full name", max_length=50)
  phone_number = models.CharField("Phone number", max_length=50)
  service = models.CharField("Service", max_length=50)
  passcat = models.CharField("Password", max_length=50)

  def __str__(self):
      return self.full_name
  
