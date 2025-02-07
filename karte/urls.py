from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    KupovinaKarteAPIView, KupljeneKarteAPIView,
    kupovinaForma, uspesna_kupovina, greska,
    karta_u_pdf, kupljene_karte, KarteViewSet
)

urlpatterns = [
    # Registracija, prijava i odjava
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # API endpoint-i
    path('api/kupovina/', KupovinaKarteAPIView.as_view(), name='kupovina-api'),
    path('api/kupljene-karte/', KupljeneKarteAPIView.as_view(), name='kupljene-karte-api'),

    # Regularni view-ovi
    path('kupovina/', kupovinaForma, name='kupovina'),
    path('uspesna-kupovina/', uspesna_kupovina, name='uspesna_kupovina'),
    path('greska/', greska, name='greska'),
    path('karta/<int:karta_id>/pdf/', karta_u_pdf, name='karta-pdf'),
    path('kupljene-karte/', kupljene_karte, name='kupljene_karte'),

    # ViewSet za REST API
    path('api/karte/', KarteViewSet.as_view({'get': 'list', 'post': 'create'}), name='karte-list'),
    path('api/karte/<int:pk>/', KarteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='karte-detail'),
]