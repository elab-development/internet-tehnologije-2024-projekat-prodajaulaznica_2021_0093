from django.contrib import admin
from .models import Utakmica

class UtakmicaAdmin(admin.ModelAdmin):
    list_display=('protivnik','datumVreme','lokacija')
# Register your models here.
admin.site.register(Utakmica, UtakmicaAdmin)