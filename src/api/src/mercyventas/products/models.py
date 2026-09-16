from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=25, decimal_places=2)
