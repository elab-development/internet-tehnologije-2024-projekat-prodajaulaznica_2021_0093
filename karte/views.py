# karte/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from reportlab.pdfgen import canvas
from .models import TipKarte, Karte, PreostaloKarata
from utakmice.models import Utakmica
from .serializers import TipKarteSerializer, KarteSerializer, PreostaloKarataSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# --- API VIEWSETOVI ---
class TipKarteViewSet(viewsets.ModelViewSet):
    queryset = TipKarte.objects.all()
    serializer_class = TipKarteSerializer

class KarteViewSet(viewsets.ModelViewSet):
    queryset = Karte.objects.all()
    serializer_class = KarteSerializer

class PreostaloKarataViewSet(viewsets.ModelViewSet):
    queryset = PreostaloKarata.objects.all()
    serializer_class = PreostaloKarataSerializer

# --- OBICAN VIEW ZA TEMPLATE ---

@login_required
def kupljene_karte(zahtev):
    kupljene = Karte.objects.filter(kupac=zahtev.user)
    return render(zahtev, 'kupljenekarte.html', {'kupljene': kupljene})


# --- API ENDPOINTI ---
@api_view(['GET'])
@permission_classes([AllowAny])
def kupovina_api(request, utakmica_id):
    try:
        utakmica = Utakmica.objects.get(id=utakmica_id)
        ostalo = PreostaloKarata.objects.filter(utakmica=utakmica)
        ostalo_data = [
            {
                'id': o.id,
                'tip_karte_id': o.tip_karte.id,
                'tip_karte': o.tip_karte.naziv,
                'preostalo': o.preostalo,
                'cena': float(o.cena)
            } for o in ostalo
        ]
        data = {
            'utakmica_id': utakmica.id,
            'utakmica': f"Partizan VS {utakmica.protivnik} - {utakmica.datumVreme.strftime('%d.%m.%Y %H:%M')}",
            'lokacija': utakmica.lokacija,
            'karte': ostalo_data
        }
        return Response(data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def register_user(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Korisnicko ime vec postoji.'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'Uspesna registracija.',
            'username': user.username,
            'email': user.email,
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def kupi_karte_api(request):
    try:
        utakmica_id = int(request.data.get('utakmica_id'))
        tip_karte_id = int(request.data.get('tip_karte_id'))
        broj_karata = int(request.data.get('broj_karata'))

        user = request.user
        utakmica = Utakmica.objects.get(id=utakmica_id)
        tip_karte = TipKarte.objects.get(id=tip_karte_id)
        preostalo = PreostaloKarata.objects.get(utakmica=utakmica, tip_karte=tip_karte)

        if preostalo.preostalo >= broj_karata:
            preostalo.preostalo -= broj_karata
            preostalo.save()

            for _ in range(broj_karata):
                Karte.objects.create(
                    tip_karte=tip_karte,
                    kupac=user,
                    utakmica=utakmica,
                    cena=preostalo.cena
                )
            return Response({'message': 'Kupovina uspesna'})
        else:
            return Response({'error': 'Nema dovoljno karata'}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def moje_karte(request):
    karte = Karte.objects.filter(kupac=request.user)
    serializer = KarteSerializer(karte, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def preuzmi_kartu_pdf(request, karta_id):
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

@login_required
def kupljene_karte_view(request):
    karte = Karte.objects.filter(kupac=request.user)
    return render(request, "kupljenekarte.html", {"karte": karte})

