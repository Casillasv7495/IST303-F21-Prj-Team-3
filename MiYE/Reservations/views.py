from django.shortcuts import render
from.models import Reservations

# Create your views here.

def show(request):
    db=Reservations.objects.all()
    return render(request, 'home.html',{'db':db})