from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField(null=True,blank=True)
    track=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(max_length=200)
    


