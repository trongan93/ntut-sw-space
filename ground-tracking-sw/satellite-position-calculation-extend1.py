# pip install skyfield basemap requests matplotlib
# pip install PyQt6

from skyfield.api import Topos, load
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Load TLE data for the ISS (you can replace with any satellite's TLE data)
satellites = load.tle_file('http://celestrak.com/NORAD/elements/stations.txt')
satellite = {sat.name: sat for sat in satellites}["ISS (ZARYA)"]

# Define observer location for context (optional)
observer = Topos('52.5200 N', '13.4050 E')  # Example: Berlin, Germany

# Get the current time and calculate the satellite position
ts = load.timescale()
time = ts.now()
geocentric = satellite.at(time)

# Extract latitude and longitude
subpoint = geocentric.subpoint()
latitude = subpoint.latitude.degrees
longitude = subpoint.longitude.degrees

print(f"Satellite Position -> Latitude: {latitude}, Longitude: {longitude}")

# Plotting the satellite position on a world map
plt.figure(figsize=(10, 5))
m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgray', lake_color='aqua')

# Convert satellite position to map projection coordinates
x, y = m(longitude, latitude)
m.plot(x, y, 'bo', markersize=10, label="Satellite Position")
plt.text(x, y, '  ISS', fontsize=12, color='blue')

# Add title and legend
plt.title("Satellite Position on World Map")
plt.legend()
plt.savefig("real-time-satellite-position.png")
