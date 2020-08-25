from django.db import models,migrations

# Create your models here.

class User_data(models.Model):
    email_address_data = models.EmailField(unique=True)
    password_data = models.TextField()
    companytype_data = models.CharField(max_length=100)
    title_data = models.CharField(max_length=100)