


import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

gdf = gpd.read_file("genus_data.gpkg")

# IMPORTANT: convert to Web Mercator (required for basemaps)
gdf_web = gdf.to_crs(epsg=3857)

print(gdf_web)
fig, ax = plt.subplots(figsize=(20, 20))

# plot your animal range

animal_num = 100

print(gdf.loc[animal_num, "Genus"])

gdf_web.iloc[[animal_num]].plot(
    ax=ax,
    edgecolor="red",
    facecolor="red",
    linewidth=2
)
# Force world extent (Web Mercator limits)
ax.set_xlim(-20037508, 20037508)
ax.set_ylim(-17037508, 20037508)

# add world basemap
ctx.add_basemap(
    ax,
    source=ctx.providers.OpenStreetMap.Mapnik,
    zoom=1
)

ax.set_axis_off()

plt.savefig(
    "world_overlay.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)
plt.close(fig)


