

import geopandas as gpd
import matplotlib.pyplot as plt
from pygbif import species
from pathlib import Path
import csv

folder = "birds"
file = "birds2.gpkg"
#filename = Path(file).stem
fileheader = "birds"

gdf = gpd.read_file(file)


step_count = 100




speciesNum = 1501





while (speciesNum <= len(gdf)):
    speciesMinNum = speciesNum - 1

    speciesMaxNum = speciesMinNum + step_count

    if (len(gdf) <= speciesMaxNum):
        speciesMaxNum = len(gdf) - 1


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

    curr_gdf.to_csv('geo/'+folder+'/'+fileheader+"_"+str(speciesMinNum+1+5000)+"-"+str(speciesMaxNum+5000)+".csv")