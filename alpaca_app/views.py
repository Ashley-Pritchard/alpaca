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
	return render(request, 'imported.html')
