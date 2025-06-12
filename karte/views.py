from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import TipKarte, Karte, PreostaloKarata
from utakmice.models import Utakmica
from .serializers import TipKarteSerializer, KarteSerializer, PreostaloKarataSerializer
from django.core.exceptions import ObjectDoesNotExist


class TipKarteViewSet(viewsets.ModelViewSet):
    queryset = TipKarte.objects.all()
    serializer_class = TipKarteSerializer

class KarteViewSet(viewsets.ModelViewSet):
    queryset = Karte.objects.all()
    serializer_class = KarteSerializer

class PreostaloKarataViewSet(viewsets.ModelViewSet):
    queryset = PreostaloKarata.objects.all()
    serializer_class = PreostaloKarataSerializer

@api_view(['GET'])
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

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Korisničko ime već postoji.'}, status=400)

        User.objects.create_user(username=username, password=password)
        return Response({'message': 'Uspešno registrovan korisnik.'}, status=201)

    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def kupi_karte_api(request):
    try:
        print("PRIMLJENI PODACI:", request.data)

        utakmica_id = int(request.data.get('utakmica_id'))
        tip_karte_id = int(request.data.get('tip_karte_id'))
        broj_karata = int(request.data.get('broj_karata'))
        username = request.data.get('username')

        print("utakmica_id:", utakmica_id)
        print("tip_karte_id:", tip_karte_id)
        print("broj_karata:", broj_karata)
        print("username:", username)

        user = User.objects.get(username=username)
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
            return Response({'message': 'Kupovina uspešna'})
        else:
            return Response({'error': 'Nema dovoljno karata'}, status=400)

    except Exception as e:
        print("GRESKA NA BACKENDU:", str(e))  
        return Response({'error': str(e)}, status=500)