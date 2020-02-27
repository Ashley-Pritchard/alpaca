from django.contrib import admin
from alpaca_app.models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(Cancer_diagnosis)
admin.site.register(Sequencer)
admin.site.register(Disease)
admin.site.register(Gene)
admin.site.register(Classification)
admin.site.register(Patient_cancer)
admin.site.register(Patient_disease)
admin.site.register(Variant)
admin.site.register(Patient_variant)
admin.site.register(Variant_sequencer)
