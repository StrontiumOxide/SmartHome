from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(APIView):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта

    def get(self, request):
        projects = Project.objects.all()
        ser = ProjectSerializer(projects, many=True)
        return Response(data=ser.data)


class MeasurementViewSet(APIView):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения

    def get(self, request):
        measurements = Measurement.objects.all()
        ser = MeasurementSerializer(measurements, many=True)
        return Response(data=ser.data)
