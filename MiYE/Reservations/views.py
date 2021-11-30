from django.shortcuts import render
from.models import Reservations

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show(request):
    db=Reservations.objects.all()
    return render(request, 'home.html', {'db':db, 'name':'new guest'})

