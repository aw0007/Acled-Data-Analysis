import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# File paths
file_path = "........\\Acled\\2021-12-14-2024-12-17.csv"
output_folder = "........\\Acled\\results"

# Load the dataset
data = pd.read_csv(file_path, delimiter=";", encoding="utf-8")

# Convert event_date to datetime and extract the year
data["event_date"] = pd.to_datetime(data["event_date"], errors="coerce")
data["year"] = data["event_date"].dt.year

# Filter data for a single year (e.g., 2024)
selected_year = 2024
data_selected_year = data[data["year"] == selected_year]

# Load a shapefile for world countries
world_shapefile = gpd.datasets.get_path('naturalearth_lowres')
world = gpd.read_file(world_shapefile)

# List of unique regions
regions = data_selected_year["region"].unique()

# Generate a map for each region
for region in regions:
    # Filter data for the region
    region_data = data_selected_year[data_selected_year["region"] == region]

    # Get countries in the region from the data
    countries_in_region = region_data["country"].unique()

    # Filter the shapefile for countries in the region
    region_countries = world[world["name"].isin(countries_in_region)]

    # Create the map
    fig, ax = plt.subplots(figsize=(12, 10))
    fig.patch.set_facecolor('white')  # Set the background to white
    region_countries.plot(ax=ax, color="lightgray", edgecolor="black")  # Plot only the region's countries

    # Plot events grouped by event_type
    for event_type, group in region_data.groupby("event_type"):
        ax.scatter(
            group["longitude"],
            group["latitude"],
            alpha=0.7,  # Adjust alpha for transparency
            edgecolor="none",  # Remove edges for a softer look
            s=group["fatalities"] * 2,  # Scale size by fatalities
            label=event_type,
        )

    # Add country names at their centroids with reduced font size
    for idx, row in region_countries.iterrows():
        centroid = row["geometry"].centroid  # Get the centroid of the country
        ax.text(
            centroid.x, centroid.y,  # Position of the text
            row["name"],  # Country name
            fontsize=6,  # Reduced font size for the country name
            ha="center",  # Center align text horizontally
            va="center",  # Center align text vertically
            color="black",  # Text color
        )

    # Remove x and y axes
    ax.axis("off")

    # Add title
    plt.title(f"Event Types in {region} ({selected_year})\n(Scaled by Fatalities)", fontsize=14)

    # Add a custom legend for fatalities scale
    legend_sizes = [10, 50, 100, 200]
    for size in legend_sizes:
        plt.scatter([], [], s=size * 2, c="gray", alpha=0.7, label=f"{size} Fatalities")

    # Add the custom legend
    plt.legend(title="Fatalities Scale", loc="lower left", bbox_to_anchor=(1, 0), fontsize=9)

    # Add author and data source signature
    plt.figtext(
        0.5, 0.01,  # Adjust Y position closer to the bottom of the figure
        "Author: MSN A. Wahid | Data Source: ACLED",  # Signature text
        ha="center", fontsize=10, color="black"
    )

    # Save the plot
    output_path = f"{output_folder}\\event_types_{region.lower().replace(' ', '_')}_fatalities_scale_{selected_year}.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight", facecolor='white')
    print(f"Plot for {region} saved as {output_path}")

    # Show the plot
    plt.show()
