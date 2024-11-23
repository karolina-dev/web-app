from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from projects import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('signup/', views.signup, name='signup'),  # Registro
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Rutas de proyectos
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),

    # Rutas de tickets dentro de un proyecto
    path('projects/<int:project_id>/tickets/', views.ticket_list, name='ticket_list'),
    path('projects/<int:project_id>/tickets/create/', views.create_ticket, name='create_ticket'),
    path('projects/<int:project_id>/tickets/<int:ticket_id>/edit/', views.edit_ticket, name='edit_ticket'),
    path('projects/<int:project_id>/tickets/history/', views.ticket_history, name='ticket_history'),
    path('projects/<int:project_id>/tickets/<int:ticket_id>/cancel/', views.cancel_ticket, name='cancel_ticket'),

    # Crear User Story
    path('projects/<int:project_id>/create_user_story/', views.create_user_story, name='create_user_story'),
]


