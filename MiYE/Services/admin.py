from django.contrib import admin

#Relative import- import Services class from models.py
from .models import Services

# Register your models here.
admin.site.register(Services)

