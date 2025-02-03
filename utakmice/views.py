from django.shortcuts import render
from rest_framework import viewsets
from utakmice.models import Utakmica
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Utakmica
from .serializers import UtakmicaSerializer

def pocetna(zahtev):
    sort_option = zahtev.GET.get('sort')
    if sort_option in ['protivnik', 'datumVreme', 'lokacija']:
        tekme = Utakmica.objects.all().order_by(sort_option)
    else:
        tekme = Utakmica.objects.all()
    return render(zahtev,'index.html',{'tekme':tekme})

@api_view(['GET'])
def utakmice_list(request):
    utakmice = Utakmica.objects.all()
    serializer = UtakmicaSerializer(utakmice, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def utakmica_create(request):
    if request.method == 'POST':
        serializer = UtakmicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def utakmica_detail(request, pk):
    try:
        utakmica = Utakmica.objects.get(pk=pk)
    except Utakmica.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UtakmicaSerializer(utakmica)
    return Response(serializer.data)

class UtakmicaViewSet(viewsets.ModelViewSet):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer