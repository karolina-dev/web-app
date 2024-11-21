from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='users'
    )

    def __str__(self):
        return self.username  # Usa el campo de AbstractUser para identificar


class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='projects'
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class UserStory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="user_stories"
    )

    def __str__(self):
        return self.title


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('En Proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
    ]

    user_story = models.ForeignKey(
        UserStory, on_delete=models.CASCADE, related_name='tickets'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()  # Descripción general del ticket
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Activo')
    comments = models.TextField(blank=True, null=True)  # Comentarios adicionales
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tickets"
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de actualización

    def __str__(self):
        return self.title
