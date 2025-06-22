from rest_framework import serializers
from .models import Utakmica

class UtakmicaSerializer(serializers.ModelSerializer):
    naziv = serializers.SerializerMethodField()

    class Meta:
        model = Utakmica
        fields = ["id", "protivnik", "datumVreme", "lokacija", "urlSlike", "naziv"]

    def get_naziv(self, obj):
        return f"Partizan VS {obj.protivnik} - {obj.datumVreme.strftime('%d.%m.%Y %H:%M')}"