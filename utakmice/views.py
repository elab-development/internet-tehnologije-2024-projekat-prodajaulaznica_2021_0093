from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Utakmica
from .serializers import UtakmicaSerializer
from karte.form import FormaKupovina
from karte.models import PreostaloKarata, Karte
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class UtakmicaViewSet(viewsets.ModelViewSet):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer

def pocetna(request):
    sort_option = request.GET.get("sort")
    if sort_option in ["protivnik", "datumVreme", "lokacija"]:
        tekme = Utakmica.objects.all().order_by(sort_option)
    else:
        tekme = Utakmica.objects.all()
    return render(request, "index.html", {"tekme": tekme})

@login_required(login_url='/login/')  # ← garantuje redirekciju ako nije ulogovan
def buypage_view(request):
    utakmica_id = request.GET.get("id")
    utakmica = get_object_or_404(Utakmica, id=utakmica_id)
    ostalo = PreostaloKarata.objects.filter(utakmica=utakmica)

    if request.method == "POST":
        forma = FormaKupovina(request.POST)
        if forma.is_valid():
            tip_karte = forma.cleaned_data["tip_karte"]
            broj_karata = int(forma.cleaned_data["broj_karata"])
            preostalo = PreostaloKarata.objects.get(utakmica=utakmica, tip_karte=tip_karte)

            if preostalo.preostalo >= broj_karata:
                preostalo.preostalo -= broj_karata
                preostalo.save()

                for _ in range(broj_karata):
                    Karte.objects.create(
                        tip_karte=tip_karte,
                        kupac=request.user,
                        utakmica=utakmica,
                        cena=preostalo.cena,
                    )
                messages.success(request, "Kupovina uspešna!")
                return redirect("pocetna")
            else:
                messages.error(request, "Nema dovoljno karata.")
    else:
        forma = FormaKupovina()

    return render(request, "kupovina.html", {
        "tekma": utakmica,
        "ostalo": ostalo,
        "forma": forma,
    })