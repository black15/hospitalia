from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
import mysql.connector

@receiver(post_save, sender=Reservation) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        
        cnx = mysql.connector.connect(host='localhost', user='root', database='hospital')
        cursor = cnx.cursor()
        add_reserv = ("INSERT INTO actions "
                    "(patient, service, doctor, visit_time, state)"
                    "VALUES (%s, %s, %s, %s, 1)")

        reservation_data = (instance.patient.full_name, instance.doctor.service, instance.doctor.full_name ,instance.reservation_date)

        # Insert new patient to mysql db
        cursor.execute(add_reserv, reservation_data)
        emp_no = cursor.lastrowid

        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()

@receiver(post_delete, sender=Reservation)
def create_profile(sender, instance, **kwargs):
    
    cnx = mysql.connector.connect(host='localhost', user='root', database='hospital')
    cursor = cnx.cursor()
    query = "DELETE FROM actions WHERE patient = %s"
    reservation_id = instance.patient.full_name
    cursor.execute(query, (reservation_id,))

    cnx.commit()

    cursor.close()
    cnx.close()