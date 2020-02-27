from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class patient(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField(null=True, blank=True)
	choices = [('yes', 'yes'), ('no', 'no'), ('unknown', 'unknown')]
	proband = models.CharField(max_length = 7, default = 'Unknown', choices=choices)
	affected_relatives = models.CharField(max_length = 7, default = 'Unknown', choices=choices)

class cancer_diagnosis(models.Model):
	stage = models.IntegerField(null=True, blank=True)
	description = models.CharField(max_length=500)

class sequencer(models.Model):
	choices = [('MiSeq', 'MiSeq'), ('HiSeq', 'HiSeq'), ('unknown', 'unknown')]
	sequencer = models.CharField(max_length = 100, default = 'unknown', choices=choices)
	
class disease(models.Model):
	disease = models.CharField(max_length = 100)

class gene(models.Model):
	gene = models.CharField(max_length = 100)
	chromosome = models.CharField(max_length = 5)

class classification(models.Model):
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
	pp6 = models.CharField(max_length = 3, default = 'no', choices=choices)
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

class patient_cancer(models.Model):
	patient_id = models.ForeignKey(patient, on_delete = models.SET_NULL, null=True, blank=True)
	cancer_diagnosis = models.ForeignKey(cancer_diagnosis, on_delete = models.SET_NULL, null=True, blank=True)

class patient_disease(models.Model):
	patient_id = models.ForeignKey(patient, on_delete = models.SET_NULL, null=True, blank=True)
	disease_id = models.ForeignKey(patient_cancer, on_delete = models.SET_NULL, null=True, blank=True)

class variant(models.Model):
	p_name = models.CharField(max_length = 100)
	c_name = models.CharField(max_length = 100)
	g_name = models.CharField(max_length = 100)
	gene_id = models.ForeignKey(gene, on_delete = models.SET_NULL, null=True, blank=True)
	classification = models.ForeignKey(classification, on_delete = models.SET_NULL, null = True, blank=True)


class patient_variant(models.Model):
	patient_id = models.ForeignKey(patient, on_delete = models.SET_NULL, null=True, blank=True)
	disease_id = models.ForeignKey(variant, on_delete = models.SET_NULL, null=True, blank=True)

class variant_sequencer(models.Model):
	variant_id = models.ForeignKey(variant, on_delete = models.SET_NULL, null=True, blank=True)
	sequencer_id = models.ForeignKey(sequencer, on_delete = models.SET_NULL, null=True, blank=True)
























