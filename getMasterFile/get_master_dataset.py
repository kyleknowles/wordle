


import geopandas as gpd
import pandas as pd

gdf = gpd.read_file("master_animal.gpkg")
df = pd.read_csv("animalDataset.csv")

merged = gdf.merge(df,
                   left_on="Genus",
                   right_on="Animal",
                   how="inner",
                   )

print(merged)