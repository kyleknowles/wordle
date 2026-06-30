


import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

gdf = gpd.read_file("birds.gpkg")

# IMPORTANT: convert to Web Mercator (required for basemaps)
gdf_web = gdf.to_crs(epsg=3857)

fig, ax = plt.subplots(figsize=(10, 10))

# plot your bird range
gdf_web.iloc[[0]].plot(
    ax=ax,
    edgecolor="red",
    facecolor="red",
    linewidth=2
)

# add world basemap
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

ax.set_axis_off()

plt.savefig("world_overlay.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.show()


