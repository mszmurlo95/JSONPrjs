import requests
#import pprint
from requests.exceptions import HTTPError
import json
import math
from geopy import distance


class StatusCode():

	def __init__(self, URL, key, locale):

		self.URL = URL
		self.key = key
		self.locale = locale

#connects to database and handles an exception if there is a connection issue
#returns a coordinate of the earthquake event
	def status_connection_attempt_do_stuff(self):


		try:
			r = requests.get(self.URL)
			print(f'Response is: {r}')
			print(f'Connection error is: {r.raise_for_status()}')
			
			data = json.loads(r.text)

			for key, items in data.items():
				if key == self.key:
					for i in items: 
						alloccurances = (i['geometry']['coordinates'])
						del alloccurances[0]
						#print(alloccurances)
						flat_distance = distance.distance(alloccurances[:2], self.locale[:2]).mi
						print(flat_distance)


						#int_flat_distance = int(flat_distance)
						
							


					

			print(type(data))
			

		except HTTPError as http_err:
			print(f'HTTP error occured: {http_err}')

		except Exception as err:
			print(f'Other error occured: {err}')
			return 0



#define class attributes
allTodaysEarthquakeData = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
dictkey = 'features'
localeToCompare = (40.167206, -105.101929) #Coordinates of Longmont, CO


allEarthquakeDataCheck = StatusCode(allTodaysEarthquakeData, dictkey, localeToCompare)
allEarthquakeDataStatus = allEarthquakeDataCheck.status_connection_attempt_do_stuff()
















