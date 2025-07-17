from django.urls import path
from .views import LoginView, LogoutView, logout_view, login_form_view

urlpatterns = [
   path('login/', login_form_view, name='login_form'),
    path('logout/', logout_view, name='logout'), 
]
