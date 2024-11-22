from django.contrib import admin
from django.urls import path, include
from . import views  # Tus propias vistas

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('signup/', views.signup, name='signup'),  # Registro
    path('accounts/', include('django.contrib.auth.urls')),  # Rutas de autenticación predeterminadas
    path('projects/', include([
        path('', views.project_list, name='project_list'),
        path('create/', views.create_project, name='create_project'),
        path('<int:pk>/', views.project_detail, name='project_detail'),
        path('<int:pk>/edit/', views.edit_project, name='edit_project'),
        path('<int:project_id>/tickets/', include([
            path('', views.ticket_list, name='ticket_list'),
            path('create/', views.create_ticket, name='create_ticket'),
            path('<int:ticket_id>/edit/', views.edit_ticket, name='edit_ticket'),
            path('history/', views.ticket_history, name='ticket_history'),
            path('<int:ticket_id>/cancel/', views.cancel_ticket, name='cancel_ticket'),
        ])),
    ])),
    path('projects/<int:project_id>/create_user_story/', views.create_user_story, name='create_user_story'),
]

