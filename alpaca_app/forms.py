from django import forms
from django.contrib import messages
from .models import *
import re

class VariantSearchForm(forms.Form):

	variant_c_input = forms.CharField(label='Variant Description', required=False)

	variant_g_input = forms.CharField(label='Variant Description', required=False)

	variant_p_input = forms.CharField(label='Variant Description', required=False)

	gene_input = forms.CharField(label='Variant Description', required=False)

	region_input = forms.CharField(label='Variant Description', required=False)


