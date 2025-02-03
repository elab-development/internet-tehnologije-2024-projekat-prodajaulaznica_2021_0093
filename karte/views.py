# karte/views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import KarteSerializer, PreostaloKarataSerializer
from .models import Karte, PreostaloKarata
from utakmice.models import Utakmica
from karte.form import FormaKupovina, RegisterForm
from rest_framework import viewsets


# Registrovanje korisnika
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Logovanje korisnika
def login_view(request):
    error_message = None 
    if request.method == "POST":  
        username = request.POST.get("username")  
        password = request.POST.get("password")  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'  
            return redirect(next_url) 
        else:
            error_message = "Invalid credentials"  
    return render(request, 'accounts/login.html', {'error': error_message})

# Log out korisnika
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

# Kupovina karata - API View za kupovinu
class KupovinaKarteAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Samo prijavljeni korisnici mogu da kupe karte

    def post(self, request, format=None):
        # Prvo, uzimamo podatke o tipu karte i broju karata
        tip_karte = request.data.get('tip_karte')
        kolicina = request.data.get('broj_karata')
        utakmica_id = request.data.get('utakmica_id')
        
        # Pretražujemo PreostaloKarata model
        izbor = get_object_or_404(PreostaloKarata, utakmica=utakmica_id, tip_karte=tip_karte)
        
        if izbor.preostalo >= int(kolicina):
            izbor.preostalo -= int(kolicina)
            izbor.save()

            # Kreiramo nove karte
            for _ in range(int(kolicina)):
                Karte.objects.create(
                    tip_karte=izbor.tip_karte,
                    kupac=request.user,
                    cena=izbor.cena,
                    utakmica=get_object_or_404(Utakmica, id=utakmica_id)
                )

            return Response({"message": "Karte su uspešno kupljene"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Nema dovoljno karata"}, status=status.HTTP_400_BAD_REQUEST)

# API View za prikaz kupljenih karata
class KupljeneKarteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        kupljene_karte = Karte.objects.filter(kupac=request.user)
        serializer = KarteSerializer(kupljene_karte, many=True)
        return Response(serializer.data)

# Forma za kupovinu karata (regularni view)
@login_required
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
                for _ in range(kolicina):
                    Karte.objects.create(
                        tip_karte=izbor.tip_karte,
                        kupac=zahtev.user,
                        cena=izbor.cena,
                        utakmica = get_object_or_404(Utakmica, id=zahtev.GET.get('id'))
                    )
                return redirect('uspesna_kupovina')
            else:
                return redirect('greska')
    else:
        utakmica_id = zahtev.GET.get('id')  # Uzimanje ID-a iz GET parametra
        utakm = get_object_or_404(Utakmica, id=utakmica_id)
        forma = FormaKupovina()
        ostalo = PreostaloKarata.objects.filter(utakmica=utakm)
    return render(zahtev,'kupovina.html',{'forma':forma,'ostalo':ostalo,'tekma':utakm})

# Uspesna kupovina
def uspesna_kupovina(zahtev):
    return render(zahtev,'uspesna-kupovina.html')

# Greška stranica
def greska(zahtev):
    return render(zahtev,'greskapage.html')

# PDF generacija za kupljenu kartu
def karta_u_pdf(request, karta_id):
    karta = get_object_or_404(Karte, id=karta_id, kupac=request.user)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="karta_{karta.id}.pdf"'
    
    p = canvas.Canvas(response)
    p.drawString(100, 750, "Karta")
    p.drawString(100, 730, f"Tip karte: {karta.tip_karte}")
    p.drawString(100, 710, f"Cena: {karta.cena} RSD")
    p.drawString(100, 690, f"Kupac: {request.user.username}")
    p.drawString(100, 670, f"Utakmica: {karta.utakmica}")

    p.save()
    return response

def kupljene_karte(request):
    # Tvoj kod za prikazivanje kupljenih karata
    return render(request, 'ime_template.html')

class KarteViewSet(viewsets.ModelViewSet):
    queryset = Karte.objects.all()
    serializer_class = KarteSerializer