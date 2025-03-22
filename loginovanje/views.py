from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from register.models import Korisnik


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            korisnik = Korisnik.objects.get(username=username, password=password)
        except Korisnik.DoesNotExist:
            return Response(
                {"error": "Pogrešno korisničko ime ili lozinka"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Generišemo JWT token
        refresh = RefreshToken.for_user(korisnik)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "username": korisnik.username,
                "email": korisnik.email,
            }
        )


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Uspešno ste se odjavili"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)