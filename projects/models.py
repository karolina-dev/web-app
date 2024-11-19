from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    # Relacionar el usuario con una compañía
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField()

    def __str__(self):
        return self.name

class UserStory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="user_stories")

    def __str__(self):
        return self.title

# No es necesario importar Ticket al principio; lo podemos hacer usando el nombre del modelo en formato de cadena.
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('En Proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
    ]

    user_story = models.ForeignKey('UserStory', on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=255)
    description = models.TextField()  # Puede ser una descripción general del ticket
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Activo')
    comments = models.TextField(blank=True, null=True)  # Este campo para los comentarios adicionales
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de actualización

    def __str__(self):
        return self.title
