from django.db import models

# ALWAYS run "python manage.py makemigrations" and "python manage.py migrate"
# Create your models here.
class Reservations(models.Model):
    guest=models.CharField(max_length=40)
    service=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    timing=models.CharField(max_length=40)
    t_service=models.CharField(max_length=20)
    room=models.CharField(max_length=20)
    city=models.CharField(max_length=30)

    def __str__(self):
        return self.guest