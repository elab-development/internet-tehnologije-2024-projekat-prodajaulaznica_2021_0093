from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"tipkarte", views.TipKarteViewSet, basename='tipkarte')
router.register(r"karte", views.KarteViewSet, basename='karte')
router.register(r"preostalo", views.PreostaloKarataViewSet, basename='preostalo')

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/kupovina/<int:utakmica_id>/", views.kupovina_api, name="kupovina_api"),
    path("api/kupovina/kupi/", views.kupi_karte_api, name="kupi_karte_api"),
    path("api/register/", views.register_user, name="register_user"),

]
