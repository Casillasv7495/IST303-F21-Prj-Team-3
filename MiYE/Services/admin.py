from django.contrib import admin

#Relative import- import Services class from models.py
from .models import Services, Types, Options

# Register your models here.
admin.site.register(Services)
admin.site.register(Types)
admin.site.register(Options)

