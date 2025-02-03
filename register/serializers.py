from rest_framework import serializers
from .models import Korisnik

class KorisnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ['id', 'username', 'password', 'email', 'brojKartice']

    def create(self, validated_data):
        korisnik = Korisnik.objects.create_user(**validated_data)
        return korisnik
