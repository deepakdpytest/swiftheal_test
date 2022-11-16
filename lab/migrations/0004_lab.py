# Generated by Django 3.1.4 on 2020-12-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lab', '0003_lab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('Lab_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=12)),
                ('Type_of_Lab', models.CharField(max_length=50)),
                ('Address', models.TextField()),
                ('Pincode', models.CharField(max_length=6)),
                ('State', models.CharField(max_length=20)),
                ('Room_No', models.CharField(max_length=10)),
                ('Lab_name', models.CharField(max_length=50)),
                ('Doctor_id', models.CharField(max_length=6)),
            ],
        ),
    ]