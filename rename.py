import glob
import re
import os


pdf_filenames = glob.glob('*.pdf')
for pdf_filename in pdf_filenames:
	print(pdf_filename)
	#new_name='dop-'+pdf_filename
	#new_name=new_name.replace(' ','_')
	new_name=re.sub('.pdf','_avis_technique.pdf',pdf_filename)
	print(new_name)
	os.rename(pdf_filename,new_name)
