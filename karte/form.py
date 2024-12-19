from django import forms
from .models import TipKarte

class FormaKupovina(forms.Form):
    tip_karte = forms.ModelChoiceField(
        queryset=TipKarte.objects.all(),
        label="Izaberite tip karte/karata"
    )
    broj_karata = forms.ChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
        label="Broj karata",
    )