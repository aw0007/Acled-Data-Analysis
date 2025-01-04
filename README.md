
# ACLED Data Analysis: Mapping Event Types by Region and Year

This repository contains the Python script and replication files for the **ACLED Data Analysis** project. The project visualizes conflict event data from the Armed Conflict Location & Event Data Project (ACLED), focusing on event types, their geographic distribution, and fatalities for a selected year and region.

---

## Project Overview

The script generates regional maps that visualize event types, scaling the event points by the number of fatalities. Each region’s map highlights countries involved in conflicts and plots events geographically, categorized by event type. The visualizations provide insights into conflict patterns and severity within each region.

---

## Repository Structure

- **Data Folder**:
  - Contains the ACLED dataset (`2021-12-14-2024-12-17.csv`).
- **Scripts Folder**:
  - Contains the Python script for mapping and analysis.
- **Results Folder**:
  - Contains the output maps for each region, saved as `.png` files.

---

## Key Features of the Analysis

- **Dynamic Year and Region Selection**:
  - The script filters events for a specific year (e.g., 2024).
  - It generates a separate map for each unique region.

- **Interactive Mapping**:
  - Plots events by geographic coordinates.
  - Differentiates event types using color-coded scatter points.
  - Scales scatter point size by the number of fatalities.

- **Region and Country Visualization**:
  - Highlights only the countries in the region on the map.
  - Annotates country names at their centroids for clarity.

- **Custom Legends**:
  - Includes a legend to scale fatalities, aiding interpretation of event severity.

---

## Generated Maps

For each region, the output map shows:
1. **Geographic Distribution**:
   - Countries involved in the region, plotted with light gray and black edges.
2. **Conflict Events**:
   - Scatter points for events, categorized by event type and scaled by fatalities.
3. **Annotations**:
   - Country names displayed at their centroids for quick identification.

Each map is saved in the `Results` folder with filenames following the format:
```
event_types_<region_name>_fatalities_scale_<year>.png
```

Example:
```
event_types_africa_fatalities_scale_2024.png
```

---

## Tools and Libraries Used

- **Python Libraries**:
  - `pandas`: For data handling and preprocessing.
  - `matplotlib`: For visualization and plotting.
  - `geopandas`: For geographic shapefile manipulation and mapping.

---

## How to Run the Script

1. **Set Up Input Files**:
   - Place the ACLED dataset (`2021-12-14-2024-12-17.csv`) in the specified folder.
   - Ensure all necessary Python libraries are installed.

2. **Run the Script**:
   - Modify `selected_year` in the script to set the year of interest.
   - Execute the script to generate maps for all regions in the dataset.

3. **View and Save Output**:
   - Output maps are saved in the `Results` folder.
   - Maps are displayed after generation for review.

---

## Sample Outputs

- **Africa**:  
  ![Sample Map for Africa](results/sample_africa_2024.png)

- **Asia**:  
  ![Sample Map for Asia](results/sample_asia_2024.png)

---

## Credits

- **Author**: Massaoudou Namata Abdoul Wahid (MSN A. Wahid)  
- **Data Source**: [ACLED](https://acleddata.com)

