from rest_framework import serializers
 from register.models import Korisnik
 
 class KorisnikSerializer(serializers.ModelSerializer):
     class Meta:
         model = Korisnik
         fields = ['id', 'username', 'email', 'brojKartice']