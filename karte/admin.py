from django.contrib import admin
from .models import Karte, TipKarte, PreostaloKarata


class TipKarteAdmin(admin.ModelAdmin):
    list_display = ("naziv",)


class PreostaloKarataAdmin(admin.ModelAdmin):
    list_display = ("utakmica", "tip_karte", "cena", "preostalo")


# Register your models here.
admin.site.register(Karte)
admin.site.register(TipKarte, TipKarteAdmin)
admin.site.register(PreostaloKarata, PreostaloKarataAdmin)
