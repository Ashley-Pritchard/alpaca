from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import numpy as np
from alpaca_app.models import *
from django.apps import apps

class Command(BaseCommand):
	help = 'Adds variant data to the database'

	def add_arguments(self, parser):
		parser.add_argument('--inputfile', dest='inputfile', required=True, help='Input file')

	def handle(self, *args, **kwargs):
		inputfile = kwargs['inputfile']
		FileImport(inputfile)

class FileImport():

	def load_df(self, filepath):

		df = pd.read_csv(filepath, sep='\t', index_col=False)

		return(df)

	def print_filepath(self, filepath):

		print("Importing file: " + filepath)

	def import_patients(self, df):

		cols = [
				'first_name',
				'last_name',
				'Age',
				'Proband',
				'affected_relatives'
			]

		df = df[cols]
		df = df.drop_duplicates()

		for row in df.itertuples():

			# if patient.objects.filter(first_name=row.first_name, last_name=row.last_name, age=row.Age).exists():
			# 	pass

			# else:
			patient, created = Patient.objects.get_or_create(
															first_name=row.first_name,
															last_name=row.last_name,
															age=row.Age,
															proband=row.Proband,
															affected_relatives=row.affected_relatives

														)						

	def import_cancer_diagnosis(self, df):

		cols = [
				'Stage',
				'Description'
			]	

		df = df[cols]
		df = df.drop_duplicates()

		for row in df.itertuples():

			cancer_diagnosis, created = Cancer_diagnosis.objects.get_or_create(
																				stage=row.Stage,
																				description=row.Description

																			)
	def import_sequencer(self, df):

		cols = ['Sequencer']


		df = df[cols]
		df = df.drop_duplicates()

		for row in df.itertuples():

			sequencer, created = Sequencer.objects.get_or_create(sequencer=row.Sequencer)

	def import_disease(self, df):

		cols = ['disease']


		df = df[cols]
		df = df.drop_duplicates()

		for row in df.itertuples():

			disease, created = Disease.objects.get_or_create(disease=row.disease)


	def import_gene(self, df):

		cols = [
				'gene',
				'chromosome'
			]


		df = df[cols]
		df = df.drop_duplicates()

		for row in df.itertuples():

			gene, created = Gene.objects.get_or_create(
														gene=row.gene,
														chromosome=row.chromosome
													)


	def import_classification(self, df):


		for row in df.itertuples():

			classification, created = Classification.objects.get_or_create(
																	user=row.user,
																	pvs1=row.PVS1,
																	ps1=row.PS1,
																	ps2=row.PS2,
																	ps3=row.PS3,
																	ps4=row.PS4,
																	pm1=row.PM1,
																	pm2=row.PM2,
																	pm3=row.PM3,
																	pm4=row.PM4,
																	pm5=row.PM5,
																	pm6=row.PM6,
																	pp1=row.PP1,
																	pp2=row.PP2,
																	pp3=row.PP3,
																	pp4=row.PP4,
																	pp5=row.PP5,
																	ba1=row.BA1,
																	bs1=row.BS1,
																	bs2=row.BS2,
																	bs3=row.BS3,
																	bs4=row.BS4,
																	bp1=row.BP1,
																	bp2=row.BP2,
																	bp3=row.BP3,
																	bp4=row.BP4,
																	bp5=row.BP5,
																	bp6=row.BP6,
																	bp7=row.BP7

																)



	def import_patient_cancer(self, df):


		for row in df.itertuples():

			patient = Patient.objects.get(					
											first_name=row.first_name,
											last_name=row.last_name,
											age=row.Age,
											proband=row.Proband,
											affected_relatives=row.affected_relatives
										)

			cancer = Cancer_diagnosis.objects.get(stage=row.Stage, description=row.Description)


			print(patient.id)
			patient_cancer, created = Patient_cancer.objects.get_or_create(
																patient_id=patient,
																cancer_diagnosis_id=cancer
															)

	def import_patient_disease(self, df):


		for row in df.itertuples():

			patient = Patient.objects.get(					
											first_name=row.first_name,
											last_name=row.last_name,
											age=row.Age,
											proband=row.Proband,
											affected_relatives=row.affected_relatives
										)

			disease = Disease.objects.get(disease=row.disease)



			patient_disease, created = Patient_disease.objects.get_or_create(
																patient_id=patient,
																disease_id=disease
															)

	def import_variants(self, df):


		for row in df.itertuples():

			gene = Gene.objects.get(
										gene=row.gene,
										chromosome=row.chromosome
									)

			criteria = Classification.objects.get(
													user=row.user,
													pvs1=row.PVS1,
													ps1=row.PS1,
													ps2=row.PS2,
													ps3=row.PS3,
													ps4=row.PS4,
													pm1=row.PM1,
													pm2=row.PM2,
													pm3=row.PM3,
													pm4=row.PM4,
													pm5=row.PM5,
													pm6=row.PM6,
													pp1=row.PP1,
													pp2=row.PP2,
													pp3=row.PP3,
													pp4=row.PP4,
													pp5=row.PP5,
													ba1=row.BA1,
													bs1=row.BS1,
													bs2=row.BS2,
													bs3=row.BS3,
													bs4=row.BS4,
													bp1=row.BP1,
													bp2=row.BP2,
													bp3=row.BP3,
													bp4=row.BP4,
													bp5=row.BP5,
													bp6=row.BP6,
													bp7=row.BP7

													)


			variant, created = Variant.objects.get_or_create(
														p_name=row.variant_protein,
														g_name=row.variant_genome,
														c_name=row.variant_cdna,
														classification=row.pathogenicity_code,
														criteria=criteria,
														gene_id=gene
													)

	def import_patient_variant(self, df):


		for row in df.itertuples():

			patient = Patient.objects.get(					
											first_name=row.first_name,
											last_name=row.last_name,
											age=row.Age,
											proband=row.Proband,
											affected_relatives=row.affected_relatives
										)

			variant = Variant.objects.get(
											p_name=row.variant_protein,
											g_name=row.variant_genome,
											c_name=row.variant_cdna,
											classification=row.pathogenicity_code,
											criteria=criteria,
											gene_id=gene
											)



			patient_variant, created = Patient_variant.objects.get_or_create(
																patient_id=patient,
																variant_id=variant
															)

	def import_variant_sequencer(self, df):


		for row in df.itertuples():


			variant = Variant.objects.get(
											p_name=row.variant_protein,
											g_name=row.variant_genome,
											c_name=row.variant_cdna,
											classification=row.pathogenicity_code,
											criteria=criteria,
											gene_id=gene
										)


			sequencer = Sequencer.objects.get(sequencer=row.Sequencer)



			sequencer, created = variant_sequencer.objects.get_or_create(
																sequencer_id=sequencer,
																variant_id=variant
															)










																	
																	



				

				



	def __init__(self, filepath):
		self.print_filepath(filepath)
		df = self.load_df(filepath)
		self.import_patients(df)
		self.import_cancer_diagnosis(df)
		self.import_sequencer(df)
		self.import_disease(df)
		self.import_gene(df)
		self.import_classification(df)
		self.import_patient_cancer(df)
		self.import_patient_disease(df)
		self.import_variants(df)


