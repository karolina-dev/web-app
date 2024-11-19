from django.shortcuts import render
from projects.models import Company

def home(request):
    # Aquí puedes agregar cualquier lógica que desees
    return render(request, 'projects/home.html')
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'projects/company_list.html', {'companies': companies})

