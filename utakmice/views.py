from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Utakmica
from .serializers import UtakmicaSerializer

# Regularni Django view za početnu stranicu
def pocetna(request):
    sort_option = request.GET.get('sort')
    if sort_option in ['protivnik', 'datumVreme', 'lokacija']:
        tekme = Utakmica.objects.all().order_by(sort_option)
    else:
        tekme = Utakmica.objects.all()
    return render(request, 'index.html', {'tekme': tekme})

# API view za listu svih utakmica
@api_view(['GET'])
def utakmice_list(request):
    utakmice = Utakmica.objects.all()
    serializer = UtakmicaSerializer(utakmice, many=True)
    return Response(serializer.data)

# API view za kreiranje nove utakmice
@api_view(['POST'])
def utakmica_create(request):
    if request.method == 'POST':
        serializer = UtakmicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view za detalje utakmice
@api_view(['GET'])
def utakmica_detail(request, pk):
    utakmica = get_object_or_404(Utakmica, pk=pk)
    serializer = UtakmicaSerializer(utakmica)
    return Response(serializer.data)

# ViewSet za CRUD operacije nad utakmicama
class UtakmicaViewSet(viewsets.ModelViewSet):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer