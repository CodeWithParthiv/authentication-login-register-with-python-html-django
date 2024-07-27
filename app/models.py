from django.db import models

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    # phone = models.CharField(max_length=10)