from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KorisnikViewSet

router = DefaultRouter()
router.register(r'korisnici', KorisnikViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
