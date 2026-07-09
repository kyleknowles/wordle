

import geopandas as gpd
import matplotlib.pyplot as plt
from pygbif import species
from pathlib import Path
import csv

folder = "fishes"
fileheader = "fishes"
file = "fishes.gpkg"
#filename = Path(file).stem

speciesNum = 1
step_count = 100


gdf = gpd.read_file(file)



while (speciesNum <= len(gdf)):
    speciesMinNum = speciesNum - 1

    speciesMaxNum = speciesMinNum + step_count

    if (len(gdf) <= speciesMaxNum):
        speciesMaxNum = len(gdf)


    vernacularNamesList = []

    curr_gdf = gdf.iloc[speciesMinNum:speciesMaxNum]
    species_list = curr_gdf["name"].to_list()

    for scientificName in species_list:
        res = species.name_backbone(scientificName=scientificName)
        if "usage" in res: 
            key = res["usage"]["key"] 
            details = species.name_usage(key=key) 
            vernacularName = details.get("vernacularName") 
            print(str(speciesNum) + ": " + str(scientificName) + ": " + str(vernacularName)) 
            vernacularNamesList.append(vernacularName)
        else:
            vernacularNamesList.append("")
            with open ("geo/errorvalues.csv", "a") as f:
                f.write(scientificName + '\n') 
        speciesNum = speciesNum + 1

    curr_gdf["Vernacular Name"] = vernacularNamesList

    curr_gdf.to_csv('geo/animals/'+folder+'/'+fileheader+"_"+str(speciesMinNum+1)+"-"+str(speciesMaxNum)+".csv")