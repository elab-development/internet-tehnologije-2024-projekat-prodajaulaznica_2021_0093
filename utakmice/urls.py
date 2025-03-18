from django.urls import path
from . import views

urlpatterns = [
    path('', views.pocetna, name='home'),  # Ova ruta će pozivati funkciju pocetna
]
