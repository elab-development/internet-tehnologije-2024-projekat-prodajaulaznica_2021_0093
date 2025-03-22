from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UtakmicaViewSet

router = DefaultRouter()
router.register(r"utakmice", UtakmicaViewSet)

urlpatterns = [
    path("", views.pocetna, name="home"),
    path("api/", include(router.urls)), 
]
