

import pandas as pd
from pathlib import Path
import re

foldername = "fishes"


path = Path("animals/" + foldername)

animal_list_c = []
animal_list_ae = []
animal_list_a_e = []


curr_genus = "Tuna"
for file in path.iterdir():

    df = pd.read_csv(file)
    curr_list = df["Vernacular Name"].to_list()

    species_list_c = [animal.capitalize() for animal in curr_list if curr_genus.upper() in str(animal).upper()] # genus in name
    species_list_ae = [animal.capitalize() for animal in curr_list if str(animal).split(" ")[-1].capitalize() == curr_genus] # genus at end of name
    species_list_a_e = [animal.capitalize() for animal in curr_list if re.split(r"[ -]",str(animal))[-1].capitalize() == curr_genus] # genus at end of name not including "-"
    

    animal_list_c = animal_list_c + species_list_c
    animal_list_ae = animal_list_ae + species_list_ae
    animal_list_a_e = animal_list_a_e + species_list_a_e

print(animal_list_c)
print()
print(animal_list_ae)
print()
print(animal_list_a_e)