import gpxpy
import folium
import numpy as np
from sklearn.cluster import DBSCAN

def read_gps_gpx_file(file_path):
    with open(file_path, 'r') as file:
        gpx_data = file.read()

    gpx = gpxpy.parse(gpx_data)

    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                latitude = point.latitude
                longitude = point.longitude
                time = point.time

                points.append({"latitude": latitude, "longitude": longitude, "time": time})

    return points

def cluster_gps_points(points, epsilon=0.01, min_samples=5):
    # Extract coordinates as numpy array
    coordinates = np.array([[point["latitude"], point["longitude"]] for point in points])

    # Apply DBSCAN clustering
    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples, metric='haversine')
    dbscan.fit(np.radians(coordinates))

    # Assign cluster labels to points
    for point, label in zip(points, dbscan.labels_):
        point["cluster_label"] = label

    return points

def map_gps_details_clustered(points, map_filename="gps_map_clustered.html"):
    # Default location for Bangalore
    initial_location = [12.9716, 77.5946]
    map_object = folium.Map(location=initial_location, zoom_start=10)

    # Use a set to store unique cluster labels
    unique_clusters = set()

    for point in points:
        cluster_label = point.get("cluster_label", None)

        # Skip points not assigned to any cluster
        if cluster_label is None:
            continue

        # Check if the cluster label is unique
        if cluster_label not in unique_clusters:
            latitude = point["latitude"]
            longitude = point["longitude"]
            time = point["time"].strftime("%Y-%m-%d %H:%M:%S")

            folium.Marker([latitude, longitude], popup=f"Time: {time}").add_to(map_object)
            unique_clusters.add(cluster_label)

    # Draw adaptive lines connecting the markers
    for cluster_label in unique_clusters:
        cluster_points = [point for point in points if point.get("cluster_label", None) == cluster_label]
        folium.PolyLine(locations=[[point["latitude"], point["longitude"]] for point in cluster_points],
                        color='blue', weight=2.5, opacity=1).add_to(map_object)

    map_object.save(map_filename)

if __name__ == "__main__":
    gpx_file_path = r"D:\Project\Speech Emotion Recognition\converted_data.gpx"  # Replace with the actual path to your GPX file

    gps_points = read_gps_gpx_file(gpx_file_path)
    clustered_gps_points = cluster_gps_points(gps_points)
    map_gps_details_clustered(clustered_gps_points)

    print("GPS details mapped. Open 'gps_map_clustered.html' in your web browser to view the map.")
