from django.db import models

# Create your models here.
class Review(models.Model):
    username=models.CharField(max_length=500,null=True,blank=True)
    Description=models.CharField(max_length=5000,null=True,blank=True)

class Registration(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=8,null=True,blank=True)
    Confirm_Password=models.CharField(max_length=8,null=True,blank=True)