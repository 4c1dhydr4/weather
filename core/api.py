from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import City, Weather
from .serializers import CitySerializer


class CityViewSet(viewsets.ViewSet):
	"""
	Viewset to expose the City Weather API
	GET and POST available
	"""
	serializer_class = CitySerializer

	def list(self, request):
		queryset = City.objects.all()
		serializer = self.serializer_class(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = City.objects.filter(pk=pk)
		city = get_object_or_404(queryset, pk=pk)
		serializer = self.serializer_class(city)
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)