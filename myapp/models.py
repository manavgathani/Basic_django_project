from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    remarks=models.CharField(max_length=50)

class User(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile_pic/',default="")