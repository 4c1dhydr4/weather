from django.contrib import admin
from django.urls import path
from rest_framework import routers
from core.views import CityView, CityWebsocket
from core.api import CityViewSet

urls = [
    path('', CityView.as_view(), name='city'),
    path('websocket', CityWebsocket.as_view(), name='websocket'),
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'api/v1/city', CityViewSet, basename='cities')

urlpatterns = urls + router.urls