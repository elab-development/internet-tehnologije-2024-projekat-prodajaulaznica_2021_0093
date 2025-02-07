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

# Registracija korisnika
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Korisnik sa ovim korisničkim imenom već postoji.')
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Prijava korisnika
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
            error_message = "Pogrešno korisničko ime ili lozinka."
    return render(request, 'accounts/login.html', {'error': error_message})

# Odjava korisnika
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

# API za kupovinu karata
class KupovinaKarteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        tip_karte = request.data.get('tip_karte')
        kolicina = request.data.get('broj_karata')
        utakmica_id = request.data.get('utakmica_id')

        try:
            izbor = PreostaloKarata.objects.get(utakmica=utakmica_id, tip_karte=tip_karte)
            if izbor.preostalo >= int(kolicina):
                izbor.preostalo -= int(kolicina)
                izbor.save()

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
        except PreostaloKarata.DoesNotExist:
            return Response({"message": "Nevažeći tip karte ili utakmica."}, status=status.HTTP_400_BAD_REQUEST)

# API za prikaz kupljenih karata
class KupljeneKarteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        kupljene_karte = Karte.objects.filter(kupac=request.user)
        serializer = KarteSerializer(kupljene_karte, many=True)
        return Response(serializer.data)

# Forma za kupovinu karata
@login_required
def kupovinaForma(request):
    if request.method == 'POST':
        form = FormaKupovina(request.POST)
        if form.is_valid():
            tip_karte = form.cleaned_data['tip_karte']
            kolicina = form.cleaned_data['broj_karata']
            utakmica_id = request.GET.get('id')
            izbor = get_object_or_404(PreostaloKarata, utakmica=utakmica_id, tip_karte=tip_karte)

            if izbor.preostalo >= kolicina:
                izbor.preostalo -= kolicina
                izbor.save()

                for _ in range(kolicina):
                    Karte.objects.create(
                        tip_karte=izbor.tip_karte,
                        kupac=request.user,
                        cena=izbor.cena,
                        utakmica=get_object_or_404(Utakmica, id=utakmica_id)
                    )

                return redirect('uspesna_kupovina')
            else:
                return redirect('greska')
    else:
        utakmica_id = request.GET.get('id')
        utakmica = get_object_or_404(Utakmica, id=utakmica_id)
        form = FormaKupovina()
        ostalo = PreostaloKarata.objects.filter(utakmica=utakmica)

    return render(request, 'kupovina.html', {'forma': form, 'ostalo': ostalo, 'utakmica': utakmica})

# Uspesna kupovina
def uspesna_kupovina(request):
    return render(request, 'uspesna-kupovina.html')

# Greška stranica
def greska(request):
    return render(request, 'greskapage.html')

# Generisanje PDF-a za kartu
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

# Prikaz kupljenih karata
@login_required
def kupljene_karte(request):
    kupljene_karte = Karte.objects.filter(kupac=request.user)
    return render(request, 'kupljene_karte.html', {'kupljene_karte': kupljene_karte})

# ViewSet za REST API
class KarteViewSet(viewsets.ModelViewSet):
    queryset = Karte.objects.all()
    serializer_class = KarteSerializer
    permission_classes = [IsAuthenticated]