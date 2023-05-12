import os

directory = "/home/reda/Desktop/ASTRAL_FT/"

for filename in os.listdir(directory):
    # new_filename="DOP-"+filename
    new_filename =filename.replace(".pdf","_fiche_technique.pdf")#.replace("_AURO_FT","").replace("-fichetechnique","")#.replace("fr-np-","")
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    print(new_filename)
# import os

# directory = "/home/reda/Desktop/ISOPROC_FT"

# for filename in os.listdir(directory):
#     if not filename.endswith(".pdf"):
#         new_filename = filename + ".pdf"
#         os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
