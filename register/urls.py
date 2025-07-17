from django.urls import path
from .views import RegisterView, register_form_view

urlpatterns = [
    path('', RegisterView.as_view(), name='api_register'),
    path('form/', register_form_view, name='register_form'),
]
