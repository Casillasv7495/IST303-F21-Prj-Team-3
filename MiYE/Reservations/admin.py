from django.contrib import admin

#Relative import- import Services class from models.py
from .models import Reservations
from .models import Customer
from .models import Order
from .models import OrderItem
from .models import Address



# Register your models here.
admin.site.register(Reservations)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)

