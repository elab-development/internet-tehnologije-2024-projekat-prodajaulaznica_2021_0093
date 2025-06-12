from django.contrib import admin
from django.urls import path, include
from karte import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Frontend deo (Django templates)
    path("", include("utakmice.urls")),
    path("karte/", include("karte.urls")),
    
    # API deo:
    path("api/register/", include("register.urls")),
    path("api/auth/", include("loginovanje.urls")),
    path("api/", include("api.urls")),


    # JWT tokeni 
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
