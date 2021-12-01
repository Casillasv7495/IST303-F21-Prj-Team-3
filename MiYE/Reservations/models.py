import uuid
from django.db import models


# ALWAYS run "python manage.py makemigrations" and "python manage.py migrate"
# Create your models here.

class Reservations(models.Model):
    SERVICES_SWEDISH = 'SW'
    SERVICES_SHIATSU = 'SH'
    SERVICES_DEEP_TISSUE = 'DT'
    SERVICES_NORMAL = 'NO'
    SERVICES_COLLAGEN ='CO'
    SERVICES_HOT_STONE = 'HS'
    SERVICES_SUGAR = 'SU'
    SERVICES_SCRUB = 'SC'
    SERVICES_HERBAL_BODY_WRAP = 'HB'
    SERVICES_BONTANICAL_MUD_WRAP = 'BM'

    SERVICES = [
        (SERVICES_SWEDISH, 'Swedish'),
        (SERVICES_SHIATSU, 'Shiatsu'),
        (SERVICES_DEEP_TISSUE, 'Deep Tissue'),
        (SERVICES_NORMAL, 'Normal'),
        (SERVICES_COLLAGEN,'Collagen'),
        (SERVICES_HOT_STONE,'Hot Stone'),
        (SERVICES_SUGAR, 'Sugar'),
        (SERVICES_SCRUB, 'Scrub'),
        (SERVICES_HERBAL_BODY_WRAP, 'Herbal Body Wrap'),
        (SERVICES_BONTANICAL_MUD_WRAP, 'Bontanical Mud Wrap'),
    ]
    id = models.CharField(max_length=255, primary_key=True, unique=True, editable=False)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    service=models.CharField(max_length=4, choices=SERVICES, default=SERVICES_NORMAL)

    def __str__(self) -> str:
        return self.id

class Customer (models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEBMERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEBMERSHIP_GOLD, 'Gold'),
    ]
    id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
    def __str__(self) -> str:
        return self.id


class Order (models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices= PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.placed_at

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    reservations = models.ForeignKey(Reservations, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.order

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    zip = models.CharField(max_length=255, default= '00000')

    def __str__(self) -> str:
        return self.street
 

