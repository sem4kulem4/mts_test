from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import ModelA, ModelB, ModelC
from .serializers import ModelASerializer, ModelBSerializer, ModelCSerializer


class ModelAList(ListCreateAPIView):
    queryset = ModelA.objects.all()
    serializer_class = ModelASerializer


class ModelBList(ListCreateAPIView):
    queryset = ModelB.objects.all()
    serializer_class = ModelBSerializer


class ModelCList(ListCreateAPIView):
    queryset = ModelC.objects.all()
    serializer_class = ModelCSerializer