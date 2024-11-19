from django.urls import path
from . import views  # Importando las vistas desde views.py


urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.company_list, name='company_list'),  # Definiendo la URL para la vista
]


