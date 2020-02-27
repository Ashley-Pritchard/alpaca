import subprocess
import argparse
import csv
import os, fnmatch
import sys
import operator as op
import pandas as pd
import numpy as np
import configparser


class ReformatData(object):

	def __init__(self, **kwargs):

		self.variants_file = kwargs['file']


	def run(self):

		variants = self.load_file()

		variants = self.split_name(variants=variants)

		variants = self.split_criteria(variants=variants)

		variants = self.expand_y_n(variants=variants)

		variants = variants.drop('Unnamed: 10', axis=1)

		PATH = os.path.dirname(os.path.realpath(__file__))
		filename = self.variants_file.split('/')[-1].split('.')[0]
		variants_seed = os.path.join(PATH, '..', '..', filename + '_seed.tsv')


		variants.to_csv(variants_seed, sep='\t')


	def load_file(self):

		variants = pd.read_csv(self.variants_file, sep='\t')

		return(variants)


	def split_name(self, variants):

		print(variants)

		variants['first_name'] = variants['Name'].apply(lambda x: x.split()[0])

		variants['last_name'] = variants['Name'].apply(lambda x: x.split()[1])

		variants = variants.drop('Name', axis=1)

		return(variants)

	def split_criteria(self, variants):

		cols = [

					'pvs1', 
					'ps1', 
					'ps2', 
					'ps3',
					'ps4', 
					'pm1', 
					'pm2', 
					'pm3',
					'pm4', 
					'pm5', 
					'pm6', 
					'pp1', 
					'pp2', 
					'pp3',
					'pp4', 
					'pp5',
					'pp6', 
					'ba1', 
					'bs1', 
					'bs2', 
					'bs3', 
					'bs4', 
					'bp1', 
					'bp2',
					'bp3', 
					'bp4', 
					'bp5', 
					'bp6', 
					'bp7' 
				]

		for col in cols:
				variants[col.upper()] = 'no'

		for value, row in variants.iterrows():

			try:
				criteria_list = row['Evidence Codes'].split(',')
			except AttributeError:
				pass

			for criteria in criteria_list:

				variants.at[value, criteria] = 'yes'

		return(variants)

	def expand_y_n(self, variants):

		alts_dict = {
							'Y': 'yes',
							'N': 'no',
							np.NaN: 'unknown'

							}

		variants['Proband'] = variants['Proband'].apply(lambda x: alts_dict[x])

		variants['Affected Relatives'] = variants['Affected Relatives'].apply(lambda x: alts_dict[x])

		return(variants)




if __name__ == '__main__':

	# location of current script
	PATH = os.path.dirname(os.path.realpath(__file__))
	variants_file = os.path.join(PATH, '..', '..', 'brca_data.tsv')
	reformatter = ReformatData(file=variants_file)
	reformatter.run()
