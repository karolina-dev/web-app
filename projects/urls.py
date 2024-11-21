from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # Página de registro
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/edit/<int:pk>/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/tickets/', views.ticket_list, name='ticket_list'),
    path('projects/<int:project_id>/tickets/create/', views.create_ticket, name='create_ticket'),
    path('create_user_story/<int:project_id>/', views.create_user_story, name='create_user_story'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('ticket_history/<int:project_id>/', views.ticket_history, name='ticket_history'),
    path('cancel_ticket/<int:ticket_id>/', views.cancel_ticket, name='cancel_ticket'),
]

