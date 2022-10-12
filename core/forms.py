from django import forms
from .models import City, Weather
from .handlers import CityHandler


class CitySelectForm(forms.Form):
	"""
	This form is used in websocket test view to select the city
	"""
	city = forms.ChoiceField()

	def __init__(self, *args, **kwargs):
		super(CitySelectForm, self).__init__(*args, **kwargs)
		choices = [(q['id'], q['name']) for q in City.objects.values()]
		self.fields['city'].choices = choices		


class CityForm(forms.ModelForm):
	"""
	This form is used to create a new city by name
	"""
	class Meta:
		model = City
		fields = ('name',)
		widgets = {
			'name': forms.TextInput(attrs={'placeholder':'City Name'}),
		}

	def clean(self):
		"""Check if the city name is valid or already exist"""

		cleaned_data = super().clean()
		name = cleaned_data.get("name")

		message = CityHandler.validate_city_name(name)

		if message:
			self.add_error('name', message)

		if City.objects.filter(name=name.title()).exists():
			self.add_error('name', 'City {} already exist'.format(name))
