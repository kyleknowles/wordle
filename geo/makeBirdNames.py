

import geopandas as gpd
import matplotlib.pyplot as plt
from pygbif import species
from pathlib import Path


file = "birds.gpkg"
filename = Path(file)

gdf = gpd.read_file(file)


step_count = 10




speciesNum = 1





while (speciesNum <= len(gdf)):
    speciesMinNum = speciesNum - 1
    speciesMaxNum = speciesMinNum + step_count


    vernacularNamesList = []

    curr_gdf = gdf.iloc[speciesMinNum:speciesMaxNum]
    species_list = curr_gdf["name"].to_list()

    for scientificName in species_list: 
        res = species.name_backbone(scientificName=scientificName) 
        key = res["usage"]["key"] 
        details = species.name_usage(key=key) 
        vernacularName = details.get("vernacularName") 
        print(str(speciesNum) + ": " + str(scientificName) + ": " + str(vernacularName)) 
        vernacularNamesList.append(vernacularName) 
        speciesNum = speciesNum + 1

    curr_gdf["Vernacular Name"] = vernacularNamesList

    curr_gdf.to_csv('geo/birds/'+str(speciesMinNum+1)+"-"+str(speciesMaxNum))