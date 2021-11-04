from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('new/', views.show) 
]