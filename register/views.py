from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import KorisnikSerializer

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        # Provera da li korisnik sa istim korisničkim imenom već postoji
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Korisnik sa ovim korisničkim imenom već postoji."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Provera da li korisnik sa istim email-om već postoji
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Korisnik sa ovim email-om već postoji."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validacija i čuvanje korisnika
        serializer = KorisnikSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "Korisnik uspešno registrovan.", "user_id": user.id},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)