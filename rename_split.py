import os

# Specify the directory where the files are located
directory = '/home/reda/Desktop/SIPLAST_FT'

for filename in os.listdir(directory):
    if "Notice" in filename:
        new_filename = filename.split("Notice",1)[0] + '_fiche_technique.pdf'
        print(new_filename)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
print("All files have been renamed")
