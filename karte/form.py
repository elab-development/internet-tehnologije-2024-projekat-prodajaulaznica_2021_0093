from django import forms
from .models import TipKarte
from django.contrib.auth.models import User


class FormaKupovina(forms.Form):
    tip_karte = forms.ModelChoiceField(
        queryset=TipKarte.objects.all(), label="Izaberite tip karte/karata"
    )
    broj_karata = forms.ChoiceField(
        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4")],
        label="Broj karata",
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, label="Unesite zeljenu lozinku"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Opet unesite lozinku"
    )

    class Meta:
        model = User
        fields = ["username", "password", "password_confirm"]
        help_texts = {
            "username": "",
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
