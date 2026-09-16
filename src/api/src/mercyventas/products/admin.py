from django.contrib import admin

# Register your models here.
from .models import Product

# test
admin.site.register(Product)
