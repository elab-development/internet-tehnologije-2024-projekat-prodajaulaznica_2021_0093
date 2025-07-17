from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Profil
from .serializers import KorisnikSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Profil

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        broj_kartice = request.data.get('brojKartice')

        if not username or not password or not email or not broj_kartice:
            return Response({"error": "Sva polja su obavezna."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Korisničko ime već postoji."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        Profil.objects.create(user=user, broj_kartice=broj_kartice)

        refresh = RefreshToken.for_user(user)

        user_data = KorisnikSerializer(user).data

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user_data
        }, status=status.HTTP_201_CREATED)
def register_form_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        broj_kartice = request.POST.get("broj_kartice")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Korisničko ime već postoji."})

        user = User.objects.create_user(username=username, password=password, email=email)
        Profil.objects.create(user=user, broj_kartice=broj_kartice)
        login(request, user)
        return redirect("pocetna")

    return render(request, "register.html")

