from django.shortcuts import render, get_object_or_404
from .models import Company, Project

def home(request):
    """Página principal."""
    return render(request, 'projects/home.html')

def company_list(request):
    """Vista para listar todas las empresas."""
    companies = Company.objects.all()
    return render(request, 'projects/company_list.html', {'companies': companies})

def company_detail(request, company_id):
    """Vista para mostrar los detalles de una empresa, incluyendo sus proyectos."""
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'projects/company_detail.html', {'company': company})

def project_detail(request, project_id):
    """Vista para mostrar los detalles de un proyecto, incluyendo sus historias de usuario."""
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})


