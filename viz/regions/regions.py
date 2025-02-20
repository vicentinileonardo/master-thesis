import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import contextily as ctx

# Load country boundaries
world = gpd.read_file("110m_cultural/ne_110m_admin_0_countries.shp")
#print(world.columns)
print(world[['ADMIN']].to_string(index=False))

# Load carbon intensity data
carbon_data = pd.read_csv('carbon_intensity_2024.csv')  # Ensure this CSV contains 'country' and 'carbon_intensity' columns

# Merge datasets
world = world.merge(carbon_data, how='left', left_on='ADMIN', right_on='country')


# Plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax)
world.plot(column='carbon_intensity', 
           ax=ax, 
           legend=True,
           legend_kwds={'label': "gCO₂eq Emissions per kWh (gCO2eq/kWh)",
                        'orientation': "horizontal",
                        'pad': 0.05,      # Moves it higher (reduce if needed)
                        'shrink': 0.75    # Adjusts the length of the color bar
                        },
           cmap='RdYlGn_r',  # Red to green colormap
           missing_kwds={"color": "lightgrey"})

# Load Azure data center locations
azure_data = pd.read_csv('azure/azure_data_centers.csv')  # Ensure this CSV contains 'latitude' and 'longitude' columns
azure_gdf = gpd.GeoDataFrame(azure_data, geometry=gpd.points_from_xy(azure_data.longitude, azure_data.latitude))

# Plot Azure data centers
#azure_gdf.plot(ax=ax, color='#FFFF00', markersize=50, label='Azure Data Centers', alpha=1.0)

ax.scatter(
    azure_gdf.geometry.x, azure_gdf.geometry.y, 
    color='#FFFF00',         # Bright yellow fill
    edgecolors='#8A2BE2',    # Violet border (BlueViolet)
    linewidth=2.0,           # Thickness of the border
    s=80,                    # Size of the marker
    label='Azure Data Centers',
    alpha=1.0,               # Full opacity
    zorder=3                 # Ensures markers are on top
)

# Add basemap
ctx.add_basemap(ax, 
                crs="EPSG:3857", 
                source=ctx.providers.OpenStreetMap.Mapnik,
                #zoom=19
                )


plt.tight_layout()


# Final touches
plt.title('Geo-distribution of Azure Data Centers and yearly Grid Carbon Intensity by Country (2024)')
plt.legend()


plt.savefig("regions.png", dpi=400, bbox_inches='tight')
plt.show()
