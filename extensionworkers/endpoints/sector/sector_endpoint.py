from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import Sector


class SectorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class SectorViewSet(ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerialiser
    permission_class = [DjangoModelPermissions]


sectorRouter = DefaultRouter()
sectorRouter.register(r'sectors', SectorViewSet)
