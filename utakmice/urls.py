from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

# Router za ViewSet
router = DefaultRouter()
router.register(r'utakmice', views.UtakmicaViewSet, 'utakmice')

urlpatterns = [
    # Regularni Django view za početnu stranicu
    path('', views.pocetna, name='home'),

    # API endpoint-i
    path('api/', include(router.urls)),  # Uključuje sve rute iz ViewSet-a

    # API view za listu svih utakmica
    path('utakmice/', views.utakmice_list, name='utakmice_list'),

    # API view za kreiranje nove utakmice
    path('utakmice/create/', views.utakmica_create, name='utakmica_create'),

    # API view za detalje utakmice
    path('utakmice/<int:pk>/', views.utakmica_detail, name='utakmica_detail'),
]