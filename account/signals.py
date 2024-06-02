from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import mysql.connector

cnx = mysql.connector.connect(host='localhost', user='root', database='hospital')
cursor = cnx.cursor()

 
@receiver(post_save, sender=Patient) 
def create_profile(sender, instance, created, **kwargs):
    if created:        
        add_patient = ("INSERT INTO patients "
                    "(full_name, phone_number, password)"
                    "VALUES (%s, %s, %s)")

        patient_data = (instance.full_name, instance.phone_number, instance.passcat)

        # Insert new patient to mysql db
        cursor.execute(add_patient, patient_data)
        emp_no = cursor.lastrowid

        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()

@receiver(post_save, sender=Doctor) 
def create_profile(sender, instance, created, **kwargs):
    if created:        

        add_doctor = ("INSERT INTO doctors "
                    "(full_name, phone, service, password)"
                    "VALUES (%s, %s, %s, %s)")

        doctor_data = (instance.full_name, instance.phone_number, instance.service, instance.passcat)

        cursor.execute(add_doctor, doctor_data)
        emp_no = cursor.lastrowid

        cnx.commit()

        cursor.close()
        cnx.close()