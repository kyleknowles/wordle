

import pandas as pd
from pathlib import Path
import re

foldername = "amphibians"

path = Path("animals/" + foldername)


ani_df = pd.read_csv("KeyGenus/" + foldername + ".csv")
ani_list = ani_df["Animal"].to_list()

total_animal_list = []

total_df = pd.DataFrame()

'''
for animal in ani_list:

    animal_list_c = []
    animal_list_ae = []
    animal_list_a_e = []

    curr_genus = animal

    for file in path.iterdir():

        df = pd.read_csv(file)

        total_df = pd.concat([total_df, df])
        curr_list = df["Vernacular Name"].to_list()

        #species_list_c = [animal.capitalize() for animal in curr_list if curr_genus.upper() in str(animal).upper()] # genus in name
        species_list_ae = [animal.capitalize() for animal in curr_list if str(animal).split(" ")[-1].capitalize() == curr_genus] # genus at end of name
        #species_list_a_e = [animal.capitalize() for animal in curr_list if re.split(r"[ -]",str(animal))[-1].capitalize() == curr_genus] # genus at end of name not including "-"
        

        #animal_list_c = animal_list_c + species_list_c
        animal_list_ae = animal_list_ae + species_list_ae
        #animal_list_a_e = animal_list_a_e + species_list_a_e



    
    
    print(animal)
    #print(animal_list_c)
    #print()
    
    print(animal_list_ae)
    print()

    total_animal_list = total_animal_list + animal_list_ae
    #print(animal_list_a_e)
    #print()
    #print()
    

    print(animal)
    print("C: " + str(len(animal_list_c)))
    print("AE: " + str(len(animal_list_ae)))
    print("A-E: " + str(len(animal_list_a_e)))
    print()


    # find differences between a-e and ae
    if (len(animal_list_a_e) != len(animal_list_ae)):
        print(animal)
        print(list(set(animal_list_a_e) - set(animal_list_ae)))
        print()

    # differences between contains and at end
    if (len(animal_list_c) != len(animal_list_ae)):
        print(animal)
        print(list(set(animal_list_c) - set(animal_list_ae)))
        print()




print(len(total_animal_list))

total_df = total_df[total_df["Vernacular Name"].isin(total_animal_list)]
print(total_df)
'''


for file in path.iterdir():
    df = pd.read_csv(file)

    total_df = pd.concat([total_df, df])
    curr_list = df["Vernacular Name"].to_list()
    


    species_list_ae = [animal.capitalize() for animal in curr_list if (str(animal).split(" ")[-1].capitalize() in ani_list)] # genus at end of name
   


    total_animal_list = total_animal_list + species_list_ae
 
    '''
    print("C: " + str(len(animal_list_c)))
    print("AE: " + str(len(animal_list_ae)))
    print("A-E: " + str(len(animal_list_a_e)))
    print()


    # find differences between a-e and ae
    if (len(animal_list_a_e) != len(animal_list_ae)):
        print(animal)
        print(list(set(animal_list_a_e) - set(animal_list_ae)))
        print()

    # differences between contains and at end
    if (len(animal_list_c) != len(animal_list_ae)):
        print(animal)
        print(list(set(animal_list_c) - set(animal_list_ae)))
        print()

    '''


print(len(total_animal_list))

total_df = total_df[total_df["Vernacular Name"].str.capitalize().isin(total_animal_list)]
print(total_df)