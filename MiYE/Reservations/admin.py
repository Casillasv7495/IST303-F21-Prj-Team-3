from django.contrib import admin

#Relative import- import Services class from models.py
from .models import Reservations

# Register your models here.
admin.site.register(Reservations)
