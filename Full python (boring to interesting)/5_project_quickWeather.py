# /user/bin/python3
# Prints the weather for location.
import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
	print('Usage: Enter the location, 5_project_quickWeather.py <location>')
	sys.exit()

location = ' '.join(sys.argv[1:])


# Download the json data from OpenWeatherMap.org's API
url = 'http://samples.openweathermap.org/data/2.5/forecast/daily?q=%s&appid=b6907d289e10d714a6e88b30761fae22' %(location)
response = requests.get(url)
response.raise_for_status()


# Load Json data into python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current Weather in %s' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after Tomorrow')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
