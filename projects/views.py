from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, TicketForm, UserStoryForm, CustomUserCreationForm
from .models import Project, Ticket, UserStory
from django.contrib import messages





# Vista de inicio
def home(request):
    if request.user.is_authenticated:
        print(f'Usuario autenticado: {request.user.username}')
    else:
        print('Usuario no autenticado')
    return render(request, 'projects/home.html')
    
# Vista de registro
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Recibe los datos del formulario
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            company = form.cleaned_data.get('company')  # Obtiene la compañía seleccionada
            user.company = company  # Asocia la compañía al usuario
            user.save()  # Guarda el usuario con la compañía asociada

            login(request, user)  # Inicia sesión automáticamente después del registro

            messages.success(request, f'¡Bienvenido {user.username}!')
            return redirect('login')  # Redirige a la página principal (o la que desees)
    else:
        form = CustomUserCreationForm()  # Si es una solicitud GET, mostramos el formulario vacío

    return render(request, 'projects/signup.html', {'form': form})



#crear historia de usuario
@login_required
def create_user_story(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        user_story_form = UserStoryForm(request.POST)
        ticket_form = TicketForm(request.POST)

        if user_story_form.is_valid() and ticket_form.is_valid():
            user_story = user_story_form.save(commit=False)
            user_story.project = project
            user_story.save()

            ticket = ticket_form.save(commit=False)
            ticket.user_story = user_story
            ticket.project = project
            ticket.status = 'Activo'  # Estado predeterminado para el primer ticket
            ticket.save()

            messages.success(request, "Historia de usuario y ticket creados exitosamente.")
            return redirect('ticket_list', project_id=project.id)  # Redirigir a la lista de tickets del proyecto
        else:
            messages.error(request, "Hubo un error en la creación de la historia de usuario o el ticket.")
    else:
        user_story_form = UserStoryForm()
        ticket_form = TicketForm()

    return render(request, 'projects/create_user_story.html', {
        'user_story_form': user_story_form,
        'ticket_form': ticket_form,
    })



# Vista de proyectos
@login_required
def project_list(request):
    projects = Project.objects.all()  # Obtener todos los proyectos
    return render(request, 'projects/project_list.html', {'projects': projects})

#vista de detalles del proyecto
from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, pk):
    # Obtener el proyecto con historias de usuario y tickets asociados
    project = get_object_or_404(Project.objects.prefetch_related('user_stories', 'tickets'), pk=pk)

    return render(request, 'projects/project_detail.html', {'project': project})



# Vista de crear proyecto, validación de historias de usuario
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            
            # Validación de que el proyecto tenga al menos 3 historias de usuario
            if project.user_stories.count() < 3:
                messages.error(request, "El proyecto debe tener al menos 3 historias de usuario.")
                return redirect('create_project')
            
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/create_project.html', {'form': form})


# Vista para editar un proyecto
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/edit_project.html', {'form': form, 'project': project})


# Vista para listar los tickets de un proyecto
def ticket_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tickets = Ticket.objects.filter(project=project)
    return render(request, 'projects/ticket_list.html', {'tickets': tickets, 'project': project})


# Vista para crear un ticket
@login_required
def create_ticket(request, project_id, user_story_id=None):
    project = get_object_or_404(Project, id=project_id)
    user_story = get_object_or_404(UserStory, id=user_story_id) if user_story_id else None

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.project = project
            if user_story:
                ticket.user_story = user_story
            ticket.save()
            return redirect('ticket_list', project_id=project.id)
    else:
        form = TicketForm(initial={'user_story': user_story})

    return render(request, 'projects/create_ticket.html', {'form': form, 'project': project})


# Vista para editar un ticket
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list', project_id=ticket.user_story.project.id)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'projects/edit_ticket.html', {'form': form,'ticket': ticket})



# Vista para ver historial de tickets
def ticket_history(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tickets = Ticket.objects.filter(user_story__project=project).order_by('status')
    
    active_tickets = tickets.filter(status='Activo')
    in_progress_tickets = tickets.filter(status='En Proceso')
    finalized_tickets = tickets.filter(status='Finalizado')

    return render(request, 'projects/ticket_history.html', {
        'active_tickets': active_tickets,
        'in_progress_tickets': in_progress_tickets,
        'finalized_tickets': finalized_tickets,
        'project': project,
    })



# Vista para cancelar un ticket
def cancel_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = 'Cancelado'
    ticket.save()
    return redirect('ticket_list', project_id=ticket.user_story.project.id)

#cerrar sesion
def user_logout(request):
    logout(request)
    return redirect('home')


