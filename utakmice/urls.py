from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtakmicaViewSet
from . import views

router = DefaultRouter()
router.register(r'utakmice', UtakmicaViewSet)

urlpatterns = [
    path('', views.pocetna, name='home'),
    path('api/', include(router.urls)),  # API endpoint za utakmice
]
