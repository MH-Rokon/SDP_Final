# Generated by Django 5.0.1 on 2024-01-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
