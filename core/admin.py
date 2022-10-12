from django.contrib import admin
from .models import City, Weather


class CityAdmin(admin.ModelAdmin):
	list_display = ('id','name',)
	list_filter = tuple()
	search_fields = ('name',)
	readonly_fields = tuple()

class WeatherAdmin(admin.ModelAdmin):
	list_display = ('id','city','temperature','timestamp','description',)
	list_filter = ('city',)
	search_fields = ('city','description',)
	readonly_fields = ('city','timestamp',)


admin.site.register(City, CityAdmin)
admin.site.register(Weather, WeatherAdmin)