from django.db import models


class City(models.Model):
	"""City Model"""
	name = models.CharField(
		max_length=140, blank=False, null=False, 
		help_text="Nombre", verbose_name="Nombre")

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		super(City, self).save(*args, **kwargs)


class Weather(models.Model):
	"""Weather Model to store weather records"""
	city = models.ForeignKey(City,
		blank=False, on_delete=models.CASCADE, null=False,
		help_text="City", editable=False, related_name='weathers',
		verbose_name="City")
	timestamp = models.DateTimeField(
		blank=False, null=False, editable=False,
		help_text="Timestamp",
		verbose_name="Timestamp")
	temperature = models.DecimalField(max_digits=6, decimal_places=2,
		blank=False, help_text="Temperature Record", 
		verbose_name="Temperature")
	description = models.CharField(
		max_length=140, blank=False, null=False, 
		help_text="Nombre", verbose_name="Nombre")
	icon = models.CharField(
		max_length=4, blank=False, null=False, 
		help_text="Open Weather Icon Code", verbose_name="Icon")
	
	class Meta:
		ordering = ('-timestamp',)

	def __str__(self):
		return '[{}] {} - {}'.format(self.timestamp, self.city, self.temperature)