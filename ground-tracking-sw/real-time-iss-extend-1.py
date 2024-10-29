import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Fetch the current ISS position from the API
url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    print(f"ISS Position -> Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Error fetching data:", response.status_code)
    exit()

# Plotting the ISS position on a world map
plt.figure(figsize=(10, 5))
m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgray', lake_color='aqua')

# Convert ISS position to map projection coordinates
x, y = m(longitude, latitude)
m.plot(x, y, 'ro', markersize=10, label="ISS Position")
plt.text(x, y, '  ISS', fontsize=12, color='red')

# Add title and legend
plt.title("Real-Time ISS Position on World Map")
plt.legend()
plt.savefig("real-time-iss-position.png")
