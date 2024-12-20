from django.urls import path
from . import views
urlpatterns = [
    path('', views.kupovinaForma, name='buypage'),
    path('uspesna-kupovina',views.uspesna_kupovina, name='uspesna_kupovina'),
    path('greska', views.greska, name='greska')
]
