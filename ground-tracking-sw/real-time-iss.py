import requests

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    position = data['iss_position']
    print(f"Latitude: {position['latitude']}, Longitude: {position['longitude']}")
else:
    print("Error fetching data:", response.status_code)

