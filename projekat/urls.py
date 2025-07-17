from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Aplikacije
    path("", include("utakmice.urls")),
    path("karte/api/", include("karte.urls")),
    path("register/", include("register.urls")), 
    path("api/auth/", include("loginovanje.urls")),
    path("api/", include("api.urls")),
    path("karte/", include("karte.urls")),

    # JWT tokeni
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
