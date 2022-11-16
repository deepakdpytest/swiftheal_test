from django.db import models


class Patient(models.Model):
    Patient_AdharId = models.CharField(max_length=12,primary_key=True)
    Password = models.CharField(max_length=12)
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=1)
    Age=models.IntegerField()
    Mobile_no=models.CharField(max_length=12)
    Address = models.TextField()
    Pincode = models.CharField(max_length=6)
    State= models.CharField(max_length=20)
    email=models.CharField(max_length=60,null=True)
    def __str__(self):
        return self.Name



class Appointment(models.Model):
    Patient_AdharId=models.CharField(max_length=12)
    Doctor_Id=models.CharField(max_length=6)
    Appointment_date=models.DateField()
    Appointment_time=models.TimeField()

    def __str__(self):
        return self.Patient_AdharId
