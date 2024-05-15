# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.views import APIView
from .models import Sensor
from .serializers import SensorSerializers
from django.http import HttpRequest
from rest_framework.response import Response

class SenserAPIView(APIView):
    def get(self, request: HttpRequest):

        """
        Получить информацию о сенсере(ах).
        """

        sensors = Sensor.objects.all()
        ser = SensorSerializers(sensors, many=True)
        return Response(ser.data)
    
    def post(self, request: HttpRequest):

        """
        Создать сенсер.
        """

        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        
        if title != None and description != None:
            Sensor(title=title, description=description).save()

            return Response(
                data={
                    'status': 'Добавлен',
                    'title': title,
                    'description': description
                }
            )

        