from django.shortcuts import render
from rest_framework import viewsets
from .models import Korisnik
from .serializers import KorisnikSerializer

class KorisnikViewSet(viewsets.ModelViewSet):
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer
