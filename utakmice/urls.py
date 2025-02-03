from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from utakmice import views

router = routers.DefaultRouter()
router.register(r'utakmice', views.UtakmicaViewSet, 'utakmice')

urlpatterns = [

    path('api/', include(router.urls)),

    path('', views.pocetna, name='home'),

    # URL za listu svih utakmica
    path('utakmice/', views.utakmice_list, name='utakmice_list'),
    
    # URL za kreiranje nove utakmice
    path('utakmice/create/', views.utakmica_create, name='utakmica_create'),
    
    # URL za prikazivanje detalja utakmice
    path('utakmice/<int:pk>/', views.utakmica_detail, name='utakmica_detail'),
]
