from django.db import models

# ALWAYS run "python manage.py makemigrations" and "python manage.py migrate"
# Create your models here.

from django.db import models

# Create your models here.
class Types(models.Model):
    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name

class Options(models.Model):
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Services(models.Model):
    THIRTY = 30
    SIXTY = 60
    NINETY = 90

    DURATION_CHOICES = [
        (THIRTY,30),
        (SIXTY,60),
        (NINETY,90)
        ]
    #name = models.CharField(max_length=100) # max_length = required
    types = models.ForeignKey(Types, on_delete=models.SET_NULL, null=True)
    options = models.ForeignKey(Options, on_delete=models.SET_NULL, null=True,)
    duration = models.IntegerField(choices=DURATION_CHOICES, default=30)
    Description = models.TextField(blank=True, null=True) # blank = field req; null => db
    Price = models.DecimalField(decimal_places=2, max_digits=10)
   