import glob
import re
import os


pdf_filenames = glob.glob('/directory/*.pdf')
for pdf_filename in pdf_filenames:
	#print(pdf_filename)
	#temp=re.sub('(^[^D]*)','',pdf_filename)
	temp=pdf_filename
	print('\n'+temp)
	temp=re.sub('.pdf','_fiche_technique.pdf',temp)

	print('\n>>>>>>'+temp)

	#new_name='dop-'+pdf_filename
	#print(new_name)
	os.rename(pdf_filename,temp)
