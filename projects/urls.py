from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # General
    path('', views.home, name='home'),  # Página principal
    path('admin/', admin.site.urls),  # Administración de Django

    # Autenticación
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.signup, name='signup'),

    # Proyectos
    path('projects/', include([
        path('', views.project_list, name='project_list'),  # Listado de proyectos
        path('create/', views.create_project, name='create_project'),  # Crear un proyecto
        path('<int:pk>/edit/', views.edit_project, name='edit_project'),  # Editar un proyecto
        path('<int:project_id>/tickets/', include([
            path('', views.ticket_list, name='ticket_list'),  # Listado de tickets por proyecto
            path('create/', views.create_ticket, name='create_ticket'),  # Crear un ticket
        ])),
    ])),

    # Historias de Usuario
    path('user_stories/<int:project_id>/create/', views.create_user_story, name='create_user_story'),

    # Tickets
    path('tickets/', include([
        path('<int:ticket_id>/edit/', views.edit_ticket, name='edit_ticket'),  # Editar ticket
        path('<int:ticket_id>/cancel/', views.cancel_ticket, name='cancel_ticket'),  # Cancelar ticket
    ])),

    # Historial
    path('projects/<int:project_id>/ticket_history/', views.ticket_history, name='ticket_history'),
]

