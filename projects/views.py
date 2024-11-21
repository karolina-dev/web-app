from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, TicketForm, UserStoryForm
from .models import Project, Ticket, UserStory
from django.contrib import messages


# Vista de inicio
def home(request):
    return render(request, 'projects/home.html')


# Vista de registro
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión después del registro
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'projects/signup.html', {'form': form})


# Vista de proyectos
def project_list(request):
    projects = Project.objects.all()  # Obtener todos los proyectos
    return render(request, 'projects/project_list.html', {'projects': projects})


# Vista para crear un proyecto
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirigir al listado de proyectos
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


# Vista para crear una historia de usuario junto con el primer ticket
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
            ticket.save()

            messages.success(request, "Historia de usuario y ticket creados exitosamente.")
            return redirect('project_list')  # Redirigir al listado de proyectos
        else:
            messages.error(request, "Hubo un error en la creación de la historia de usuario o el ticket.")
    else:
        user_story_form = UserStoryForm()
        ticket_form = TicketForm()

    return render(request, 'projects/create_user_story.html', {
        'user_story_form': user_story_form,
        'ticket_form': ticket_form,
    })


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
    return render(request, 'projects/edit_ticket.html', {'form': form})


# Vista para ver historial de tickets
def ticket_history(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tickets = Ticket.objects.filter(user_story__project=project).order_by('status')
    return render(request, 'projects/ticket_history.html', {'tickets': tickets, 'project': project})


# Vista para cancelar un ticket
def cancel_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = 'Cancelado'
    ticket.save()
    return redirect('ticket_list', project_id=ticket.user_story.project.id)


