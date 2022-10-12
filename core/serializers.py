from rest_framework import serializers
from .models import (City, Weather,)
from .handlers import CityHandler


class WeatherSerializer(serializers.ModelSerializer):
	"""
	Weather serializer to expose weather data though the API
	"""
	temperature = serializers.FloatField()

	class Meta:
		model = Weather
		fields = ('timestamp', 'temperature','description','icon')


class CitySerializer(serializers.ModelSerializer):
	"""
	City serializer to expose city data though the API
	"""
	weathers = WeatherSerializer(many=True, read_only=True) # Annidate weathers for every city 
	week_avg = serializers.SerializerMethodField() # Set last 7 days temperature average

	class Meta:
		model = City
		fields = ('pk','name', 'week_avg', 'weathers',)

	def create(self, validated_data):
		city = City(**validated_data)
		city.save()
		CityHandler(city_id=city.id).update_weather()
		return city

	def validate_name(self, value):
		message = CityHandler.validate_city_name(value)
		if message:
			raise serializers.ValidationError(message)
		if City.objects.filter(name=value.title()).exists():
			raise serializers.ValidationError('City {} already exist'.format(value))
		return value

	def get_week_avg(self, obj):
		return CityHandler(city_id=obj.id).get_last_week_avg()
