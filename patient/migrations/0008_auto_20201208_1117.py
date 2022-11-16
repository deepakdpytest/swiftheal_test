# Generated by Django 3.0.5 on 2020-12-08 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_auto_20201208_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Appointment_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_time',
            field=models.TimeField(),
        ),
    ]
