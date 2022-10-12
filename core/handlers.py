import requests
from datetime import datetime, timedelta
from django.db.models import Avg
from weather.settings import OPEN_WEATHER_ID
from .models import City, Weather
from .consumers import send_weather_update


OPEN_WEATHER_URL= "http://api.openweathermap.org/data/2.5/weather?q={query}&APPID={app_id}"


class CityHandler(object):
	"""
	This python object is used to handle the city processes through the application 
	"""
	city_id = None
	city_name = None

	def __init__(self, city_id=None):
		if not city_id:
			raise Exception('Provide a city_id')
		self.city_id = int(city_id)

	def update_weather(self):
		"""
		Update the weather only if there isn't a record since 30 minutes ago
		This method should be a cronjob task in the server to avoid the load
		"""
		half_hour_ago = datetime.now() - timedelta(minutes=30)
		
		if Weather.objects.filter(city=self.city_id, timestamp__gte=half_hour_ago).exists():
			return None

		self.request_weather()

	def request_weather(self):
		"""
		Request weather from OpenWeather API
		TODO: handler request connection issues
		"""
		city = City.objects.get(pk=self.city_id)
		url = OPEN_WEATHER_URL.format(query=city.name, app_id=OPEN_WEATHER_ID)
		data = requests.get(url).json()

		if 'message' in data:
			# TODO: Log message (possible city not found)
			return None

		Weather.objects.create(
			city_id=self.city_id,
			timestamp=datetime.fromtimestamp(data['dt']),
			temperature=data['main']['temp'],
			description=data['weather'][0]['description'],
			icon=data['weather'][0]['icon']
		)

		send_weather_update(city_id=self.city_id) # Send to the channels layer

	def get_last_week_avg(self):
		"""
		Get last week temperature average for a specific city
		"""
		date_max = datetime.now()
		date_min = date_max - timedelta(days=7)
		last_seven_days_range = (date_min, date_max)
		
		query = Weather.objects.filter(
			city=self.city_id, 
			timestamp__range=last_seven_days_range
		).aggregate(Avg('temperature'))
		
		if not query['temperature__avg']:
			query['temperature__avg'] = 0
		
		return round(query['temperature__avg'], 2)


	@staticmethod
	def validate_city_name(city_name):
		"""
		Static method to validate the city name with OpenWeather API
		"""
		url = OPEN_WEATHER_URL.format(query=city_name, app_id=OPEN_WEATHER_ID)
		data = requests.get(url).json()
		
		if 'message' in data:
			return data['message']
		
		return None