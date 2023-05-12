import glob
import re
import os


pdf_filenames = glob.glob('*.pdf')
for pdf_filename in pdf_filenames:
	print(pdf_filename)
	temp=re.sub('(^[^D]*)','',pdf_filename)
	print(temp)
	#new_name='dop-'+pdf_filename
	#print(new_name)
	os.rename(pdf_filename,temp)
