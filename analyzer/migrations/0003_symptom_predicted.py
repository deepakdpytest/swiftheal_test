# Generated by Django 3.0.5 on 2020-12-08 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_auto_20201207_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='predicted',
            field=models.CharField(default='none', max_length=50),
        ),
    ]