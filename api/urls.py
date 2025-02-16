from django.urls import path
from .views import UtakmicaList, UtakmicaDetail

urlpatterns = [
    path('utakmice/', UtakmicaList.as_view(), name='utakmica-list'),
    path('utakmice/<int:pk>/', UtakmicaDetail.as_view(), name='utakmica-detail'),
]