from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KorisnikViewSet

router = DefaultRouter()
router.register(r'korisnici', KorisnikViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API rute za korisnike
]
