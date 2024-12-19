from django.shortcuts import redirect, render
from karte.form import FormaKupovina
from .models import PreostaloKarata

# Create your views here.
def kupovinaForma(zahtev):
    if zahtev.method == 'POST':
        forma = FormaKupovina(zahtev.POST)
        if forma.is_valid():
            return redirect('uspesna_kupovina')
    else:
        forma = FormaKupovina()
        ostalo = PreostaloKarata.objects.all()
    return render(zahtev,'kupovina.html',{'forma':forma,'ostalo':ostalo})

def uspesna_kupovina(zahtev):
    return render(zahtev,'uspesna-kupovina.html')