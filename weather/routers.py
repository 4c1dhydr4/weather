from django.urls import re_path
from core.consumers import (CityConsummer,)

websocket_urlpatterns = [
	re_path(r'ws/city/(?P<city_id>\w+)/$', CityConsummer.as_asgi()),
]