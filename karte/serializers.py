from rest_framework import serializers
from .models import Karte, TipKarte, PreostaloKarata
from utakmice.models import Utakmica

class TipKarteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipKarte
        fields = ['id', 'naziv']

class KarteSerializer(serializers.ModelSerializer):
    tip_karte = TipKarteSerializer(read_only=True)
    utakmica = serializers.PrimaryKeyRelatedField(queryset=Utakmica.objects.all())

    class Meta:
        model = Karte
        fields = ['id', 'tip_karte', 'kupac', 'utakmica', 'cena']

class PreostaloKarataSerializer(serializers.ModelSerializer):
    tip_karte = TipKarteSerializer(read_only=True)
    utakmica = serializers.PrimaryKeyRelatedField(queryset=Utakmica.objects.all())

    class Meta:
        model = PreostaloKarata
        fields = ['id', 'utakmica', 'tip_karte', 'preostalo', 'cena']
