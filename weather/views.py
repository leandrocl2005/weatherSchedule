from .serializers import WeatherSerializer
from .models import Weather
from rest_framework import generics


class WeatherList(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
