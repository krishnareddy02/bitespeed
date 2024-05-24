from django.db import models
from datetime import datetime
# Create your models here.

class contact(models.Model):                 
    phoneNumber=models.CharField(max_length=100)
    email=models.EmailField()
    linkedId =models.IntegerField()
    linkPrecedence=models.CharField(max_length=100)
    createdAt=models.CharField(max_length=100)             
    updatedAt=models.CharField(max_length=100)              
    deletedAt=models.CharField(max_length=100)  