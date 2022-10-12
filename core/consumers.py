import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync, sync_to_async
from .models import City, Weather

def send_weather_update(city_id):
	"""
	This function sents the weather update for a specific city
	:param int city_id: City Record id
	"""
	data = Weather.objects.filter(city_id=city_id).values('temperature','icon','description').first()
	data['temperature'] = float(data['temperature'])
	layer = get_channel_layer()
	async_to_sync(layer.group_send)('city_%s' % city_id, {'type': 'city_update', **data})


class CityConsummer(AsyncWebsocketConsumer):
	"""
	This consummer can be used with Websockets to receive weather 
	updates for a specific city
	"""
	async def connect(self):
		self.city_id = self.scope['url_route']['kwargs']['city_id']
		self.orders_group_name = 'city_%s' % self.city_id

		await self.channel_layer.group_add(
			self.orders_group_name,
			self.channel_name
		)

		await self.accept()

		await sync_to_async(send_weather_update)(self.city_id)

	async def disconnect(self, close_code):

		await self.channel_layer.group_discard(
			self.orders_group_name,
			self.channel_name
		)

	async def receive(self, text_data):
		data = json.loads(text_data)
		await self.channel_layer.group_send(
			self.orders_group_name,
			{
				'type': 'city_update',
				**data
			}
		)

	async def city_update(self, event):
		await self.send(text_data=json.dumps(event))