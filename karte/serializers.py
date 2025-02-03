# karte/serializers.py

from rest_framework import serializers
from .models import Karte, TipKarte, PreostaloKarata
from utakmice.models import Utakmica
from django.contrib.auth.models import User


class TipKarteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipKarte
        fields = ['id', 'naziv']

class UtakmicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utakmica
        fields = ['id', 'naziv', 'datum', 'mesto']  # Prilagodi polja prema svom modelu


class PreostaloKarataSerializer(serializers.ModelSerializer):
    tip_karte = TipKarteSerializer()
    utakmica = UtakmicaSerializer()

    class Meta:
        model = PreostaloKarata
        fields = ['id', 'utakmica', 'tip_karte', 'preostalo', 'cena']


class KarteSerializer(serializers.ModelSerializer):
    tip_karte = TipKarteSerializer()
    kupac = serializers.StringRelatedField()  # Možeš koristiti username ili nešto drugo
    utakmica = UtakmicaSerializer()

    class Meta:
        model = Karte
        fields = ['id', 'tip_karte', 'kupac', 'utakmica', 'cena']
