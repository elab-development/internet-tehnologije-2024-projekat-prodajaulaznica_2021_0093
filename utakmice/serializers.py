from rest_framework import serializers
from .models import Utakmica

class UtakmicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utakmica
        fields = '__all__'
