from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from karte.form import FormaKupovina
from karte.models import PreostaloKarata
from utakmice.models import Utakmica

# Create your views here.
def kupovinaForma(zahtev):
    if zahtev.method == 'POST':
        forma = FormaKupovina(zahtev.POST)
        if forma.is_valid():
            tipkarte = zahtev.POST.get('tip_karte')
            kolicina = int(zahtev.POST.get('broj_karata'))
            izbor = get_object_or_404(PreostaloKarata, utakmica=get_object_or_404(Utakmica, id=zahtev.GET.get('id')), tip_karte=tipkarte)
            if izbor.preostalo >= kolicina:
                izbor.preostalo -= kolicina
                izbor.save()
                return redirect('uspesna_kupovina')
            else:
                return redirect('greska')
    else:
        utakmica_id = zahtev.GET.get('id')  # Uzimanje ID-a iz GET parametra
        utakm = get_object_or_404(Utakmica, id=utakmica_id)
        forma = FormaKupovina()
        ostalo = PreostaloKarata.objects.filter(utakmica=utakm)
    return render(zahtev,'kupovina.html',{'forma':forma,'ostalo':ostalo,'tekma':utakm})

def uspesna_kupovina(zahtev):
    return render(zahtev,'uspesna-kupovina.html')

def greska(zahtev):
    return render(zahtev,'greskapage.html')