from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .models import City, Weather
from .forms import CityForm, CitySelectForm
from .handlers import CityHandler


class CityView(CreateView):
	"""
	This is the home view to get all cities current weathers and 
	provide a form to add more cities.
	"""
	model = City
	form_class = CityForm
	success_url = '/'
	template_name = 'city.html'

	def get_cities(self):
		cities = City.objects.values('pk','name')
		
		for city in cities:
			handler = CityHandler(city_id=city['pk'])	

			handler.update_weather()
			
			city['avg'] = handler.get_last_week_avg()
			
			city['weathers'] = Weather.objects.filter(
				city=city['pk']
			).values('timestamp', 'temperature', 'description', 'icon')[:5]
		
		return cities

	def get_context_data(self, **kwargs):
		context = super(CityView, self).get_context_data(**kwargs)
		context['cities'] = self.get_cities()
		return context


class CityWebsocket(TemplateView):
	"""
	This template view is used to test the channels layer for city consumer
	"""
	template_name = "city_socket.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CitySelectForm()
		return context
