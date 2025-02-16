from rest_framework import serializers
from utakmice.models import Utakmica

class UtakmicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utakmica
        fields = '__all__'