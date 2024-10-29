import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Example coordinates for the satellite or ISS position
latitude = 34.0522  # Replace with actual latitude
longitude = -118.2437  # Replace with actual longitude

# Set up the map with Cartopy
plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()  # Adds a base image (e.g., Earth)
ax.coastlines()

# Plot the satellite position
plt.plot(longitude, latitude, 'ro', markersize=10, transform=ccrs.PlateCarree())
plt.text(longitude + 3, latitude, 'Satellite', transform=ccrs.PlateCarree())

# Save the plot as a file instead of displaying it
plt.title("Satellite Position on World Map")
plt.savefig("satellite_position.png")
