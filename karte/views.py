from django.shortcuts import get_object_or_404, redirect, render
from karte.form import FormaKupovina
from karte.models import PreostaloKarata
from utakmice.models import Utakmica

# Create your views here.
def kupovinaForma(zahtev):
    if zahtev.method == 'POST':
        forma = FormaKupovina(zahtev.POST)
        if forma.is_valid():
            return redirect('uspesna_kupovina')
    else:
        utakmica_id = zahtev.GET.get('id')  # Uzimanje ID-a iz GET parametra
        utakm = get_object_or_404(Utakmica, id=utakmica_id)
        forma = FormaKupovina()
        ostalo = PreostaloKarata.objects.filter(utakmica=utakm)
    return render(zahtev,'kupovina.html',{'forma':forma,'ostalo':ostalo})

def uspesna_kupovina(zahtev):
    return render(zahtev,'uspesna-kupovina.html')