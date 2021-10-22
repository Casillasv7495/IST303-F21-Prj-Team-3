from django.db import models

# ALWAYS run "python manage.py makemigrations" and "python manage.py migrate"
# Create your models here.
class Services(models.Model):
    Service = models.CharField(max_length=100) # max_length = required
    Description = models.TextField(blank=True, null=True) # blank = field req; null => db
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Like = models.BooleanField(default=True)