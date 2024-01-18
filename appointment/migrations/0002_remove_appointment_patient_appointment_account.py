# Generated by Django 5.0.1 on 2024-01-17 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='account',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.usermaxaccount'),
        ),
    ]
