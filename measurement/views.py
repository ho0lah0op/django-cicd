from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, SensorDetailSerializer, \
    MeasurementCreateSerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class TemperatureMeasurementCreateView(generics.CreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = MeasurementCreateSerializer


@api_view(['GET'])
def sample_view(request):
    return Response({'message': 'Hi man!'})
