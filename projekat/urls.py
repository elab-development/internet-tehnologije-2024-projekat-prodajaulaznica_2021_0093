from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Aplikacije
    path("", include("utakmice.urls")),  # ako imaš views/template-ove
    path("karte/api/", include("karte.urls")),  # API endpointi za karte

    # Ostale API rute (ako ih imaš)
    path("api/register/", include("register.urls")),
    path("api/auth/", include("loginovanje.urls")),
    path("api/", include("api.urls")),  # dodatni api ako postoji

    # JWT tokeni
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
