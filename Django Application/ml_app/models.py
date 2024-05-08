from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=25)
    email = models.EmailField(unique = True)
    phone = models.PositiveIntegerField()
    password = models.CharField(max_length=15)