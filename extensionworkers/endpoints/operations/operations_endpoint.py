from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import Operation


class OperationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class OperationViewSet(ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerialiser
    permission_class = [DjangoModelPermissions]


operationsRouter = DefaultRouter()
operationsRouter.register(r'operations', OperationViewSet)
