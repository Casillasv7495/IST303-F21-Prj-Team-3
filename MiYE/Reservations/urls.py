from django.urls import path
from django.conf.urls import url
from . import views
from .views import(
    customer_create
    )

#URLConf
urlpatterns = [
    path('', views.show),
    path('new/', views.ReservationCreateView.as_view()),
    url(r'^create/$',customer_create)
    
]