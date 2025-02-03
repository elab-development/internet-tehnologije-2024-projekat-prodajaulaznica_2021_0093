from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Korisnik
from .serializers import KorisnikSerializer
from django.contrib.auth import authenticate, login

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = KorisnikSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return Response({'message': 'Uspesno ste se prijavili!'}, status=status.HTTP_200_OK)
    return Response({'error': 'Pogresni kredencijali!'}, status=status.HTTP_400_BAD_REQUEST)
