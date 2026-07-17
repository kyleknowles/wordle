
import pandas as pd
import geopandas as gpd
from shapely import wkt

orders = ["mammals", "reptiles", "amphibians", "birds", "fishes"]

total_gdf = gpd.GeoDataFrame()

for order in orders:
    filename = order
    df = pd.read_csv("SimplifiedGenus/"+filename+".csv")


    df["Genus"] = df["Vernacular Name"].str.split(" ").str[-1].str.capitalize()


    df["First Scientific Name"] = df["name"].str.split(" ").str[0].str.capitalize()

    front_values = ["Vernacular Name", "name", "Genus", "First Scientific Name"]

    df = df[front_values + [col for col in df.columns if col not in front_values]]

    
    if (filename == "fishes"):
        df["Order"] = "Fish"
    else:
        df["Order"] = filename[:-1].capitalize()
    

    df = df.sort_values(by=["Genus", "First Scientific Name"])

    df["geometry"] = df["geometry"].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

    gdf = gdf.dissolve(by="Genus")

    total_gdf = gpd.GeoDataFrame(
        pd.concat([total_gdf, gdf], ignore_index=True),
        crs=gdf.crs
    )

print(total_gdf)
total_gdf.to_file("master_animal.gpkg", driver="GPKG")

#df.to_csv("sortedAnimals.csv")



"""
df = df[["Vernacular Name", "name", "Genus", "First Scientific Name"]]
for value, group in df.groupby("Genus"):
    print("Value")
    for value2, group in group.groupby("First Scientific Name"):
        print(value2)
        print(group)
        print()
    print()
"""