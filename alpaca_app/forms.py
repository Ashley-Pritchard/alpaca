from django import forms
from .models import *
import re

class VariantSearchForm(forms.Form):

	variant_c_input = forms.CharField(label='Variant Description', required=False)

	variant_g_input = forms.CharField(label='Variant Description', required=False)

	variant_p_input = forms.CharField(label='Variant Description', required=False)

	gene_input = forms.CharField(label='Variant Description', required=False)


