from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Services, Options
from .forms import ServicesForm
from django.shortcuts import render

class ServicesListView(ListView):
    model = Services
    form_class = ServicesForm
    context_object_name = 'Services'

class ServicesCreateView(CreateView):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('services_changelist')

class ServicesUpdateView(UpdateView):
    model = Services
    form_class = ServicesForm  
    success_url = reverse_lazy('services_changelist')

def load_optiones(request):
    types_id = request.GET.get('types')
    optiones = Options.objects.filter(types_id=types_id).order_by('name')
    return render(request, 'Services/option_ddl.html', {'optiones': optiones})