# Import necessary libraries
from skyfield.api import Topos, load
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Load TLE data for Weather Satellites from CelesTrak
satellites = load.tle_file('http://celestrak.com/NORAD/elements/weather.txt')
satellite = {sat.name: sat for sat in satellites}["NOAA 18"]

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
m.plot(x, y, 'bo', markersize=10, label="NOAA 18 Position")
plt.text(x, y, ' NOAA 18', fontsize=12, color='blue')

# Add title and legend
plt.title("NOAA 18 Satellite Position on World Map")
plt.legend()
plt.savefig("real-time-noaa18-position.png")
