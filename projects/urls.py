from django.urls import path
from . import views  # Importa las vistas de la misma app

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('companies/', views.company_list, name='company_list'),  # Lista de empresas
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),  # Detalles de empresa
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),  # Detalles de proyecto
]

