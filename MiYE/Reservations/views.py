from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from .forms import ReservationsForm
from.models import Reservations, Customer

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show(request):
    db=Reservations.objects.all()
    return render(request, 'home.html', {'db':db})

def customer_create(request):
    form = ReservationsForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
        }
    return render(request, 'register.html', context)


   
