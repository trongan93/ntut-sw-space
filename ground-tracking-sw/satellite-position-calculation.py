# pip install skyfield
from skyfield.api import Topos, load

# Load TLE data from Celestrak or Space-Track
satellites = load.tle_file('http://celestrak.com/NORAD/elements/stations.txt')
satellite = {sat.name: sat for sat in satellites}["ISS (ZARYA)"]

# Define observer's location
observer = Topos('52.5200 N', '13.4050 E')  # Berlin, for example

# Calculate satellite position
ts = load.timescale()
time = ts.now()
difference = satellite - observer
topocentric = difference.at(time)
alt, az, distance = topocentric.altaz()

print(f"Altitude: {alt.degrees} degrees")
print(f"Azimuth: {az.degrees} degrees")
print(f"Distance: {distance.km} km")
