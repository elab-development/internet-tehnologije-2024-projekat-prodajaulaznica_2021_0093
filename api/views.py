# api/views.py
from rest_framework import generics
from utakmice.models import Utakmica
from .serializers import UtakmicaSerializer

class UtakmicaList(generics.ListCreateAPIView):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer

class UtakmicaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer
