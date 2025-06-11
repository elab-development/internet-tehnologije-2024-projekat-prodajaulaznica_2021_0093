# karte/views.py
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import TipKarte, Karte, PreostaloKarata
from .serializers import TipKarteSerializer, KarteSerializer, PreostaloKarataSerializer
from karte.form import FormaKupovina, RegisterForm
from utakmice.models import Utakmica
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view


class TipKarteViewSet(viewsets.ModelViewSet):
    queryset = TipKarte.objects.all()
    serializer_class = TipKarteSerializer

class KarteViewSet(viewsets.ModelViewSet):
    queryset = Karte.objects.all()
    serializer_class = KarteSerializer

class PreostaloKarataViewSet(viewsets.ModelViewSet):
    queryset = PreostaloKarata.objects.all()
    serializer_class = PreostaloKarataSerializer

# Register view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

# Login view
def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get("next") or request.GET.get("next") or "home"
            return redirect(next_url)
        else:
            error_message = "Invalid credentials"
    return render(request, "accounts/login.html", {"error": error_message})

# Logout view
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")

# Purchased tickets page
@login_required
def kupljene_karte(request):
    kupljene = Karte.objects.filter(kupac=request.user)  # Pronađite kupljene karte za trenutnog korisnika
    return render(request, "kupljenekarte.html", {"kupljene": kupljene})

@login_required
def kupovinaForma(request):
    if request.method == "POST":
        form = FormaKupovina(request.POST)
        if form.is_valid():
            tipkarte = request.POST.get("tip_karte")
            kolicina = int(request.POST.get("broj_karata"))
            utakmica_id = request.GET.get("id")
            utakm = get_object_or_404(Utakmica, id=utakmica_id)
            izbor = get_object_or_404(
                PreostaloKarata,
                utakmica=utakm,
                tip_karte=tipkarte,
            )
            if izbor.preostalo >= kolicina:
                izbor.preostalo -= kolicina
                izbor.save()
                for _ in range(kolicina):
                    Karte.objects.create(
                        tip_karte=izbor.tip_karte,
                        kupac=request.user,
                        cena=izbor.cena,
                        utakmica=utakm,
                    )
                return redirect("uspesna_kupovina")
            else:
                return redirect("greska")
    else:
        utakmica_id = request.GET.get("id")
        utakm = get_object_or_404(Utakmica, id=utakmica_id)
        forma = FormaKupovina()
        ostalo = PreostaloKarata.objects.filter(utakmica=utakm)
    return render(
        request, "kupovina.html", {"forma": forma, "ostalo": ostalo, "tekma": utakm}
    )

def uspesna_kupovina(request):
    return render(request, "uspesna-kupovina.html")

def greska(request):
    return render(request, "greskapage.html")

def karta_u_pdf(request, karta_id):
    karta = get_object_or_404(Karte, id=karta_id, kupac=request.user)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="karta_{karta.id}.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 750, "Karta")
    p.drawString(100, 730, f"Tip karte: {karta.tip_karte}")
    p.drawString(100, 710, f"Cena: {karta.cena} RSD")
    p.drawString(100, 690, f"Kupac: {request.user.username}")
    p.drawString(100, 670, f"Utakmica: Partizan vs {karta.utakmica.protivnik} - {karta.utakmica.datumVreme.strftime('%d.%m.%Y %H:%M')}")
    p.save()
    return response

@api_view(['GET'])
def kupljene_karte_api(request, username):
    user = User.objects.get(username=username)
    kupljene = Karte.objects.filter(kupac=user)
    serializer = KarteSerializer(kupljene, many=True)
    return Response(serializer.data)