from django.contrib import admin
from django.urls import path, include
from karte import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Aplikacije
    path("", include("utakmice.urls")),
    path("karte/", include("karte.urls")),
    path("register/", include("register.urls")),
    path("api/", include("api.urls")),
    path("api/auth/", include("loginovanje.urls")),
    # Autentifikacija
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("accounts/register/", views.register_view, name="register"),
    # JWT Tokeni
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
