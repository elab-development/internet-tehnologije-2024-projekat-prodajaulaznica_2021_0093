from django.shortcuts import get_object_or_404, redirect, render
from karte.form import FormaKupovina, RegisterForm
from karte.models import PreostaloKarata
from utakmice.models import Utakmica

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

# Create your views here.
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