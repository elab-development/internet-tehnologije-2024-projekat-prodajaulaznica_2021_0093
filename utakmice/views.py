from django.shortcuts import render
from .serializers import UtakmicaSerializer
from utakmice.models import Utakmica
from rest_framework import viewsets


# Create your views here.
def pocetna(zahtev):
    sort_option = zahtev.GET.get('sort')
    if sort_option in ['protivnik', 'datumVreme', 'lokacija']:
        tekme = Utakmica.objects.all().order_by(sort_option)
    else:
        tekme = Utakmica.objects.all()
    return render(zahtev,'index.html',{'tekme':tekme})

class UtakmicaViewSet(viewsets.ModelViewSet):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer