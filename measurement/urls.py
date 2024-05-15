from django.urls import path
from .views import SenserAPIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SenserAPIView.as_view())
]
