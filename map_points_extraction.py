import gpxpy
from gpxpy.gpx import GPXTrackPoint
from datetime import datetime

def convert_dat_to_gpx(dat_filename):
    with open(dat_filename, 'r') as dat_file:
        dat_data = dat_file.readlines()

    gpx = gpxpy.gpx.GPX()
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    # Skip the header line
    header_skipped = False

    for data_point in dat_data:
        # Skip the header line
        if not header_skipped:
            header_skipped = True
            continue

        # Check if the line contains the expected number of values
        if ',' not in data_point:
            continue  # Skip lines without commas

        timestamp_str, latitude_str, ns, longitude_str, ew, altitude_str, speed_str = data_point.strip().split(',')
        
        timestamp = datetime.strptime(timestamp_str, "%Y%m%d%H%M%S")
        latitude = float(latitude_str) * (-1 if ns == 'S' else 1)
        longitude = float(longitude_str) * (-1 if ew == 'W' else 1)
        altitude = float(altitude_str)
        speed = float(speed_str)

        gpx_point = GPXTrackPoint(latitude, longitude, elevation=altitude, time=timestamp, speed=speed)
        gpx_segment.points.append(gpx_point)

    return gpx

# Specify the path to your .dat file
dat_filename = r"D:\Vanture recording\Hessaraghatta\20240115.dat"

# Convert to GPX
gpx_data = convert_dat_to_gpx(dat_filename)

# Save the GPX data to a file
gpx_filename = "converted_data.gpx"
with open(gpx_filename, "w") as gpx_file:
    gpx_file.write(gpx_data.to_xml())

print(f"Conversion complete. GPX file saved as {gpx_filename}")
