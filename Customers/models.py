from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.

class CustomersDetails(models.Model):
    CustomerName = models.CharField(max_length=100)
    AccountNumber = models.BigIntegerField(max_length=17)
    CustomerMail = models.EmailField(max_length=100)
    Balance = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return self.CustomerName

class MyAccount(models.Model):
    MyName = models.CharField(max_length=100)
    AccountNumber = models.BigIntegerField(max_length=17)
    MyMail = models.EmailField(max_length=100)
    Balance = models.PositiveIntegerField(default=10000000)

    def __str__(self):
        return self.MyName