

import geopandas as gpd
import matplotlib.pyplot as plt
from pygbif import species


gdf = gpd.read_file("birds.gpkg")



species_list = gdf["name"].to_list()
print(species_list)


vernacularNamesList = []
speciesNum = 1


for scientificName in species_list: 
    res = species.name_backbone(scientificName=scientificName) 
    key = res["usage"]["key"] 
    details = species.name_usage(key=key) 
    vernacularName = details.get("vernacularName") 
    print(str(speciesNum) + ": " + str(scientificName) + ": " + str(vernacularName)) 
    vernacularNamesList.append(vernacularName) 
    speciesNum = speciesNum + 1