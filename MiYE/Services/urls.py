from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ServicesListView.as_view(), name='services_changelist'),
    path('add/', views.ServicesCreateView.as_view(), name='services_add'),
    path('<int:pk>/', views.ServicesUpdateView.as_view(), name='services_change'),
    path('ajax/load-optiones/', views.load_optiones, name='ajax_load_optiones'),
   ]
