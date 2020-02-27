from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField(null=True, blank=True)
	choices = [('yes', 'yes'), ('no', 'no'), ('unknown', 'unknown')]
	proband = models.CharField(max_length = 7, default = 'Unknown', choices=choices)
	affected_relatives = models.CharField(max_length = 7, default = 'Unknown', choices=choices)

class Cancer_diagnosis(models.Model):
	stage = models.IntegerField(null=True, blank=True)
	description = models.CharField(max_length=500)

class Sequencer(models.Model):
	choices = [('miseq', 'miseq'), ('hiseq', 'hiseq'), ('unknown', 'unknown')]
	sequencer = models.CharField(max_length = 100, default = 'unknown', choices=choices)
	
class Disease(models.Model):
	disease = models.CharField(max_length = 100)

class Gene(models.Model):
	gene = models.CharField(max_length = 100)
	chromosome = models.CharField(max_length = 5)

class Classification(models.Model):
	user = models.CharField(max_length = 100)
	choices = [('yes', 'yes'), ('no', 'no')]
	pvs1 = models.CharField(max_length = 3, default = 'no', choices=choices)
	ps1 = models.CharField(max_length = 3, default = 'no', choices=choices)
	ps2 = models.CharField(max_length = 3, default = 'no', choices=choices)
	ps3 = models.CharField(max_length = 3, default = 'no', choices=choices)
	ps4 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pm1 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pm2 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pm3 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pm4 = models.CharField(max_length = 3, default = 'no', choices=choices)	
	pm5 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pm6 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pp1 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pp2 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pp3 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pp4 = models.CharField(max_length = 3, default = 'no', choices=choices)
	pp5 = models.CharField(max_length = 3, default = 'no', choices=choices)
	ba1 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bs1 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bs2 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bs3 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bs4 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bp1 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bp2 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bp3 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bp4 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bp5 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bp6 = models.CharField(max_length = 3, default = 'no', choices=choices)
	bp7 = models.CharField(max_length = 3, default = 'no', choices=choices)

class Patient_cancer(models.Model):
	patient_id = models.ForeignKey(Patient, on_delete = models.SET_NULL, null=True, blank=True)
	cancer_diagnosis = models.ForeignKey(Cancer_diagnosis, on_delete = models.SET_NULL, null=True, blank=True)

class Patient_disease(models.Model):
	patient_id = models.ForeignKey(Patient, on_delete = models.SET_NULL, null=True, blank=True)
	disease_id = models.ForeignKey(Disease, on_delete = models.SET_NULL, null=True, blank=True)

class Variant(models.Model):
	p_name = models.CharField(max_length = 100)
	c_name = models.CharField(max_length = 100)
	g_name = models.CharField(max_length = 100)
	gene_id = models.ForeignKey(Gene, on_delete = models.SET_NULL, null=True, blank=True)
	classification = models.CharField(max_length=10, default='unknown')
	criteria = models.ForeignKey(Classification, on_delete = models.SET_NULL, null=True, blank=True)


class Patient_variant(models.Model):
	patient_id = models.ForeignKey(Patient, on_delete = models.SET_NULL, null=True, blank=True)
	variant_id = models.ForeignKey(Variant, on_delete = models.SET_NULL, null=True, blank=True)

class Variant_sequencer(models.Model):
	variant_id = models.ForeignKey(Variant, on_delete = models.SET_NULL, null=True, blank=True)
	sequencer_id = models.ForeignKey(Sequencer, on_delete = models.SET_NULL, null=True, blank=True)
























