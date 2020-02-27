from django.contrib import admin
from alpaca_app.models import patient, cancer_diagnosis, sequencer, disease, gene, classification, patient_cancer, patient_disease, variant, patient_variant, variant_sequencer 

# Register your models here.

admin.site.register(patient)
admin.site.register(cancer_diagnosis)
admin.site.register(sequencer)
admin.site.register(disease)
admin.site.register(gene)
admin.site.register(classification)
admin.site.register(patient_cancer)
admin.site.register(patient_disease)
admin.site.register(variant)
admin.site.register(patient_variant)
admin.site.register(variant_sequencer)
