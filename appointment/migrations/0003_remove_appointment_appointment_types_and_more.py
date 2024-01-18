# Generated by Django 5.0.1 on 2024-01-18 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('appointment', '0002_remove_appointment_patient_appointment_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_types',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='account',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='accounts.usermaxaccount'),
        ),
    ]
