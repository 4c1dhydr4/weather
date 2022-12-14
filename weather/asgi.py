import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

import django

django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .routers import websocket_urlpatterns

application = ProtocolTypeRouter({
	"http": get_asgi_application(),
	"websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
})
