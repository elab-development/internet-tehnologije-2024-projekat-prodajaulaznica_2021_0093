from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"tipkarte", views.TipKarteViewSet, basename="tipkarte")
router.register(r"karte", views.KarteViewSet, basename="karte")
router.register(r"preostalo", views.PreostaloKarataViewSet, basename="preostalo")

urlpatterns = [
    path("", include(router.urls)),  # automatski API za viewsetove
    
    # Custom API rute
    path("kupovina/<int:utakmica_id>/", views.kupovina_api, name="kupovina_api"),
    path("kupovina/kupi/", views.kupi_karte_api, name="kupi_karte_api"),
    path("register/", views.register_user, name="register_user"),
    path("moje-karte/", views.moje_karte, name="moje_karte"),
    path("karte/preuzmi/<int:karta_id>/", views.preuzmi_kartu_pdf, name="preuzmi_kartu_pdf"),
]
