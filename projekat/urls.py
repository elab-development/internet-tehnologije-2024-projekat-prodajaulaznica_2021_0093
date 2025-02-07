from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from karte import views as karte_views
from utakmice import views as utakmice_views
from loginovanje import views as login_views

# Router za DRF ViewSet-ove
router = routers.DefaultRouter()
router.register(r'karte', karte_views.KarteViewSet, 'karte')  # Registrujemo ViewSet za karte
router.register(r'utakmice', utakmice_views.UtakmicaViewSet, 'utakmice')  # Registrujemo ViewSet za utakmice

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoint-i
    path('api/', include(router.urls)),  # Uključujemo sve rute iz routera
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # DRF autentifikacija

    # Autentifikacija
    path('accounts/login/', login_views.login_view, name='login'),  # Prijava korisnika
    path('accounts/logout/', login_views.logout_view, name='logout'),  # Odjava korisnika
    path('accounts/register/', login_views.register_view, name='register'),  # Registracija korisnika

    # Aplikacije
    path('', include('utakmice.urls')),  # Uključujemo sve rute iz aplikacije `utakmice`
    path('karte/', include('karte.urls')),  # Uključujemo sve rute iz aplikacije `karte`
]