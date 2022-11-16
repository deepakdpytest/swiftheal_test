from django.db import models

class Lab(models.Model):
    Lab_id = models.CharField(max_length=6,primary_key=True)
    Password = models.CharField(max_length=12)
    Type_of_Lab = models.CharField(max_length=50)
    Address = models.TextField()
    Pincode = models.CharField(max_length=6)
    State= models.CharField(max_length=20)
    Room_No = models.CharField(max_length=10)
    Lab_name= models.CharField(max_length=50)
    Doctor_id = models.CharField(max_length=6)
     
    def __str__(self):
        return self.Lab_name
    
       

     
