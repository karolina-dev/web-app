from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Company, Project, Ticket, UserStory

# Formulario para CustomUser
class CustomUserCreationForm(UserCreationForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=True, label="Compañía")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'company', 'password1', 'password2']

# Formulario para Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

# Formulario para UserStory
class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)  
        super().__init__(*args, **kwargs)
        if project:
            self.fields['project'].initial = project

# Formulario para Ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'user_story', 'status', 'comments', 'project']

    def __init__(self, *args, **kwargs):
        user_story = kwargs.pop('user_story', None)  # Historia de usuario inicial (si se pasa desde la vista)
        super().__init__(*args, **kwargs)
        if user_story:
            self.fields['user_story'].initial = user_story  # Inicializar con la historia asociada
        self.fields['user_story'].queryset = UserStory.objects.all()  # Mostrar todas las historias existentes

