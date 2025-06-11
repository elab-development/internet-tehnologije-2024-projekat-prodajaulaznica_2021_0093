from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Korisnik

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        brojKartice = request.data.get('brojKartice')

        if not username or not password or not email or not brojKartice:
            return Response({"error": "Sva polja su obavezna."}, status=status.HTTP_400_BAD_REQUEST)

        if Korisnik.objects.filter(username=username).exists():
            return Response({"error": "Korisničko ime već postoji."}, status=status.HTTP_400_BAD_REQUEST)

        korisnik = Korisnik.objects.create(
            username=username,
            password=password,  # Ako želiš, možeš ovde dodati hash šifrovanje lozinke
            email=email,
            brojKartice=brojKartice
        )

        refresh = RefreshToken.for_user(korisnik)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": korisnik.username,
            "email": korisnik.email,
        }, status=status.HTTP_201_CREATED)
