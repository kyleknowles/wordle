
import pandas as pd
from pathlib import Path


foldername = "reptiles"

animal_list = []

path = Path("animals/" + foldername)


for file in path.iterdir():
    #print(file)

    df = pd.read_csv(file)
    curr_list = df["Vernacular Name"].to_list()

    #print(bird_list)
    #print()

    # gets last word of every 
    lastname = [str(animal).split(" ")[-1] for animal in curr_list]
    #print(lastname)
    #print()
    animal_list = animal_list + lastname


unique_last_names = list(set(animal_list))
unique_last_names.sort()
print(unique_last_names)