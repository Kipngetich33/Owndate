from django.db import models

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    bio = models.TextField()
    profile_pic = models.FilePathField(path="/img")
