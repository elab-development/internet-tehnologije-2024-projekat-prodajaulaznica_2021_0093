from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtakmicaViewSet, pocetna, buypage_view

router = DefaultRouter()
router.register(r"utakmice", UtakmicaViewSet)

urlpatterns = [
    path("", pocetna, name="pocetna"),
    path("kupovina/", buypage_view, name="buypage"),
    path("api/", include(router.urls)),
]