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

class TipKarteViewSet(viewsets.ModelViewSet):
    queryset = TipKarte.objects.all()
    serializer_class = TipKarteSerializer

class KarteViewSet(viewsets.ModelViewSet):
    queryset = Karte.objects.all()
    serializer_class = KarteSerializer

class PreostaloKarataViewSet(viewsets.ModelViewSet):
    queryset = PreostaloKarata.objects.all()
    serializer_class = PreostaloKarataSerializer

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
    return render(request, 'accounts/register.html', {'form':form})

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

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

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
        utakmica_id = zahtev.GET.get('id')
        utakm = get_object_or_404(Utakmica, id=utakmica_id)
        forma = FormaKupovina()
        ostalo = PreostaloKarata.objects.filter(utakmica=utakm)
    return render(zahtev,'kupovina.html',{'forma':forma,'ostalo':ostalo,'tekma':utakm})

def uspesna_kupovina(zahtev):
    return render(zahtev,'uspesna-kupovina.html')

def greska(zahtev):
    return render(zahtev,'greskapage.html')

def kupljene_karte(zahtev):
    if zahtev.method == "POST":
        kupljene = Karte.objects.filter(kupac=zahtev.user)
        return render(zahtev,'kupljenekarte.html',{'kupljene':kupljene})
    
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

class KarteViewSet(viewsets.ModelViewSet):
    queryset = Karte.objects.all()
    serializer_class = KarteSerializer