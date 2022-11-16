from django.db import models


class Doctor(models.Model):
    Doctor_id = models.CharField(max_length=6,primary_key=True)
    Password = models.CharField(max_length=12)
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=1)
    Age=models.IntegerField()
    Aadhar_id=models.CharField(max_length=12)
    Mobile_no=models.CharField(max_length=12)
    Email=models.TextField()
    Qualification=models.TextField()
    Area_of_specialisation=models.CharField(max_length=30)
    Year_of_experience=models.IntegerField()
    Type_of_practice=models.CharField(max_length=20)
    Hospital_id = models.CharField(max_length=6)
    photo=models.ImageField(upload_to='static/profile',null=True)
     
    def __str__(self):
        return self.Name

