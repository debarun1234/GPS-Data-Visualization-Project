# GPS-Data-Visualization-Project

## Project Overview

The goal of this project is to visualize GPS data recorded from a Vantura E3 dashcam. The GPS data is initially provided in a proprietary .dat format, and our objective is to convert it to the standard GPX format for better compatibility. After the conversion, we aim to visualize the GPS data on an interactive map, highlighting significant points such as corners and turns.

## Project Steps

### Step 1: Convert .dat to GPX

We start by converting the proprietary .dat file to the GPX format, which is a standard XML-based file format for storing GPS data.

```python
# Code Snippet for .dat to GPX Conversion
import gpxpy
from datetime import datetime

def convert_dat_to_gpx(dat_data):
    # ... (Code to convert .dat data to GPX)
    return gpx

# Sample data
dat_data = [
    "20240115090025,13.139441,N,77.568527,E,5.812,962.800",
    # Add more data points
]

gpx_data = convert_dat_to_gpx(dat_data)

```
### Step 2: Cluster GPS Points

After converting to GPX, we apply the DBSCAN algorithm to cluster GPS points. This helps identify significant points like corners and turns.

``` python
# Code Snippet for Clustering GPS Points
# (Refer to the provided code for the complete script)
import numpy as np
from sklearn.cluster import DBSCAN

def cluster_gps_points(points, epsilon=0.01, min_samples=5):
    # ... (Code to cluster GPS points using DBSCAN)
    return points
```
### Step 3: Map GPS Details

Finally, we visualize the GPS data on an interactive map using Folium. This includes placing markers at significant points and connecting them with adaptive lines

``` python
# Code Snippet for Mapping GPS Details
# (Refer to the provided code for the complete script)
import folium

def map_gps_details_clustered(points, map_filename="gps_map_clustered.html"):
    # ... (Code to map GPS details with clustering)
    return
```

### How to Run the Project
1. Replace the sample data in the conversion script with your actual .dat file data.
2. Adjust any file paths as needed.
3. Run the conversion script to obtain a GPX file.
4. Run the clustering script to identify significant points.
5. Run the mapping script to generate an interactive map.

### Output
* Conversion Script Output: filename.gpx
* Mapping Script Output: filename.html

_***Open the generated gps_map_clustered.html file in a web browser to view the interactive map._

### Credits
* Debarun Ghosh
