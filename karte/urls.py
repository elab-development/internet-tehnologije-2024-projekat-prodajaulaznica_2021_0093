from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TipKarteViewSet, KarteViewSet, PreostaloKarataViewSet

# Definiši router za ViewSet-ove
router = DefaultRouter()
router.register(r"tipkarte", TipKarteViewSet)
router.register(r"karte", KarteViewSet)
router.register(r"preostalo", PreostaloKarataViewSet)

urlpatterns = [
    path("", views.kupovinaForma, name="buypage"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path(
        "uspesna-kupovina/", views.uspesna_kupovina, name="uspesna_kupovina"
    ),  # Ispravljen duplikat
    path("greska/", views.greska, name="greska"),
    path("kupljene/", views.kupljene_karte, name="kupljene"),
    path(
        "export-pdf/<int:karta_id>/", views.karta_u_pdf, name="export"
    ),  # Ispravljen duplikat
    path("kupovina/", views.kupovinaForma, name="kupovina"),
    path("api/", include(router.urls)),
    path('api/karte/kupljene/<str:username>/', views.kupljene_karte_api),
    path("api/kupovina/<int:utakmica_id>/", views.kupovina_api, name="kupovina_api"),
    path("", views.kupovinaForma, name="buypage"),
    path("api/", include(router.urls)),
    path("api/kupovina/<int:utakmica_id>/", views.kupovina_api, name="kupovina_api"),
]
