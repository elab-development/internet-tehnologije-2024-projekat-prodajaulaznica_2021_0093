from django.urls import include, path
from .views import UtakmicaList, UtakmicaDetail

urlpatterns = [
    path("utakmice/", UtakmicaList.as_view(), name="utakmica-list"),
    path("utakmice/<int:pk>/", UtakmicaDetail.as_view(), name="utakmica-detail"),
    path("karte/", include("karte.urls")),
    path("register/", include("register.urls")),  
    path("auth/", include("loginovanje.urls")),
]
