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
	
	gene = Gene.objects.get(id=1)
	variant = Variant()
	variant.p_name = request.POST.get('p_name')
	variant.g_name = request.POST.get('g_name')
	variant.c_name = request.POST.get('c_name')
	variant.gene_id = gene
	variant.classification = request.POST.get('classification')
	variant.save()

	return render(request, 'imported.html')
