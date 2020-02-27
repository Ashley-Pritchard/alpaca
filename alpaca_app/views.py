from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
	return render(request, 'index.html')

def search(request):
	return render(request, 'search.html')

def import_variant(request):
	return render(request, 'import_variant.html')

def imported(request):
	
	patient = Patient()
	patient.first_name = request.POST.get('first_name')
	patient.last_name = request.POST.get('last_name')
	patient.age = request.POST.get('age')
	patient.proband = request.POST.get('proband')
	patient.affected_relatives = request.POST.get('affected_relatives')

	return render(request, 'imported.html')
