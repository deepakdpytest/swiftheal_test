from django.db import models



class Hospital(models.Model):
    Hospital_id = models.CharField(max_length=6,primary_key=True)
    Name_hs= models.TextField()
    State= models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Pincode = models.CharField(max_length=6)
    Address_hs= models.TextField()
    Late_fine=models.CharField(max_length=20)
    
    def __str__(self):
        return self.Name_hs
   