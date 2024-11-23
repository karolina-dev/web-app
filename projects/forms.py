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
        # Obtenemos los parámetros que podrían ser pasados desde la vista
        user_story = kwargs.pop('user_story', None)  # Historia de usuario inicial
        project = kwargs.pop('project', None)  # Proyecto inicial

        super().__init__(*args, **kwargs)

        # Si se pasa un `user_story` desde la vista, lo configuramos como valor inicial
        if user_story:
            self.fields['user_story'].initial = user_story  # Inicializamos el campo `user_story`
        
        # Si se pasa un `project` desde la vista, lo configuramos como valor inicial
        if project:
            self.fields['project'].initial = project  # Inicializamos el campo `project`

        # Establecemos el queryset de `user_story` para que solo se vean las historias de usuario del proyecto
        if project:
            self.fields['user_story'].queryset = UserStory.objects.filter(project=project)

        # Establecer el queryset para `project` (aunque podría no ser necesario en este formulario si ya lo pasas desde la vista)
        self.fields['project'].queryset = Project.objects.all()
