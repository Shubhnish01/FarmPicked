from django.db import models


class Customer_Service_Request(models.Model):
    CSR_name = models.CharField(max_length=50)
    CSR_email = models.CharField(max_length=60)
    CSR_phone = models.CharField(max_length=12)
    CSR_Subject = models.CharField(max_length=100)
    CSR_message = models.TextField()


# Create your models here.


class OrderCheckout(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=150)
    addressline2 = models.CharField(max_length=200)
    city = models.CharField(max_length=12)
    State = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)
