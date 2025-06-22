from rest_framework import serializers
from .models import Karte, TipKarte, PreostaloKarata
from utakmice.models import Utakmica
from utakmice.serializers import UtakmicaSerializer  # dodato

class TipKarteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipKarte
        fields = ["id", "naziv"]

class KarteSerializer(serializers.ModelSerializer):
    tip_karte = TipKarteSerializer(read_only=True)
    utakmica = UtakmicaSerializer(read_only=True)  # izmenjeno

    class Meta:
        model = Karte
        fields = ["id", "tip_karte", "kupac", "utakmica", "cena"]

class PreostaloKarataSerializer(serializers.ModelSerializer):
    tip_karte = TipKarteSerializer(read_only=True)
    utakmica = serializers.PrimaryKeyRelatedField(queryset=Utakmica.objects.all())

    class Meta:
        model = PreostaloKarata
        fields = ["id", "utakmica", "tip_karte", "preostalo", "cena"]