from rest_framework import serializers
from .models import Korisnik

class KorisnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = "__all__"  
