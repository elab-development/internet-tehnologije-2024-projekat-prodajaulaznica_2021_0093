# karte/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TipKarteViewSet, KarteViewSet, PreostaloKarataViewSet

# Definisanje router-a za API rute
router = DefaultRouter()
router.register(r'tipkarte', TipKarteViewSet)
router.register(r'karte', KarteViewSet)
router.register(r'preostalo', PreostaloKarataViewSet)

# URL rute za karte
urlpatterns = [
    path('', views.kupovinaForma, name='buypage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('uspesna-kupovina', views.uspesna_kupovina, name='uspesna_kupovina'),
    path('greska', views.greska, name='greska'),
    path('kupljene', views.kupljene_karte, name='kupljene'),
    path('export-pdf/<int:karta_id>/', views.karta_u_pdf, name='export'),
    path('kupovina/', views.kupovinaForma, name='kupovina'),
    
    # API rute za karte
    path('api/', include(router.urls)),  # Ovo uključuje rute iz routera za tipkarte, karte i preostalo
]
