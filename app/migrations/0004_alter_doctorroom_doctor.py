# Generated by Django 5.0.6 on 2024-05-31 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_doctor_user_alter_patient_user'),
        ('app', '0003_doctorroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorroom',
            name='doctor',
            field=models.ManyToManyField(related_name='rooms', to='account.doctor', verbose_name='Doctor'),
        ),
    ]