from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataViewSet(generics.ListAPIView):
    queryset = SensorData.objects.all().order_by('timestamp')
    serializer_class = SensorDataSerializer
