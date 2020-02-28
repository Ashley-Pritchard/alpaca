from django.shortcuts import render
from django.views import View
from .models import *
from .forms import VariantSearchForm
import pandas as pd

# Create your views here.

class index(View):

	def get(self, request):

		# empty variant search form
		form = VariantSearchForm()
		
		input_list = list(request.GET.dict().values())

		print(len(set(input_list)))

		if len(set(input_list))==2:
			form = VariantSearchForm(request.GET)

			if form.is_valid():
			
				if request.GET['gene_input']:
					# variant search form populated with request.GET data
	
				
					
					

					print(form.data)
					print('form is valid')
					gene = form.cleaned_data['gene_input']
					gene = Gene.objects.get(gene=gene)
					variants = Variant.objects.filter(gene_id=gene.id).values()


					variants_df = pd.DataFrame(list(variants))

					variants_df['gene'] = gene.gene

					variants_df = variants_df[['gene', 'p_name', 'c_name', 'g_name', 'classification']]
					variants_df = variants_df.rename(columns={'p_name': 'protein variant', 'c_name': 'cDNA variant', 'g_name': 'genomic variant'})

					variants_html = variants_df.to_html(table_id='search_results', classes='count-table style=width:100%', index=False)

					context = {'results': variants_html}
					return render(request, 'search.html', context)

				elif request.GET['variant_g_input']:
		
					
		
					input_variant = form.cleaned_data['variant_g_input']
					


					variants = Variant.objects.filter(g_name=input_variant).values()

					variants_df = pd.DataFrame(list(variants))

					for value, row in variants_df.iterrows():


						gene = Gene.objects.get(id=row.gene_id_id)

						variants_df.at[value, 'gene'] = gene.gene

					variants_df = variants_df[['gene', 'p_name', 'c_name', 'g_name', 'classification']]
					variants_df = variants_df.rename(columns={'p_name': 'protein variant', 'c_name': 'cDNA variant', 'g_name': 'genomic variant'})

					variants_html = variants_df.to_html(table_id='search_results', classes='count-table style=width:100%', index=False)

					context = {'results': variants_html}
					return render(request, 'search.html', context)


			

				elif request.GET['variant_p_input']:

					
			
					input_variant = form.cleaned_data['variant_p_input']
					


					variants = Variant.objects.filter(p_name=input_variant).values()

					variants_df = pd.DataFrame(list(variants))


					for value, row in variants_df.iterrows():

						gene = Gene.objects.get(id=row.gene_id_id)

						variants_df.at[value, 'gene'] = gene.gene

					variants_df = variants_df[['gene', 'p_name', 'c_name', 'g_name', 'classification']]
					variants_df = variants_df.rename(columns={'p_name': 'protein variant', 'c_name': 'cDNA variant', 'g_name': 'genomic variant'})

					variants_html = variants_df.to_html(table_id='search_results', classes='count-table style=width:100%', index=False)

					context = {'results': variants_html}
					return render(request, 'search.html', context)

				elif request.GET['variant_c_input']:
				
					
			

			
					input_variant = form.cleaned_data['variant_c_input']
					

					variants = Variant.objects.filter(c_name=input_variant).values()

					variants_df = pd.DataFrame(list(variants))


					for value, row in variants_df.iterrows():

						gene = Gene.objects.get(id=row.gene_id_id)

						variants_df.at[value, 'gene'] = gene.gene

					variants_df = variants_df[['gene', 'p_name', 'c_name', 'g_name']]
					variants_df = variants_df.rename(columns={'p_name': 'protein variant', 'c_name': 'cDNA variant', 'g_name': 'genomic variant'})

					variants_html = variants_df.to_html(table_id='search_results', classes='count-table style=width:100%', index=False)

					context = {'results': variants_html}
					return render(request, 'search.html', context)




			else:
				print('1')
				return render(request, 'index.html', {'form':form})

		else:
			print('2')
			return render(request, 'index.html', {'form':form})

class search(View):

	# def get(self, request):

	# 	print(request.get)
	# 	if 'input' in request.get:
	# 		# variant search form populated with request.GET data
	# 		form = VariantSearchForm(request.GET)
	# 		print(form)
	# 		# validate form data before proceeding with query
	# 		if form.is_valid():

	# 			print(form.data)
	# 			print('form is valid')

	# 	else:

	# 			print('XXXX')

	def get(self, request):
		return render(request, 'search.html')

def import_variant(request):
	return render(request, 'import_variant.html')

def imported(request):
	return render(request, 'imported.html')
