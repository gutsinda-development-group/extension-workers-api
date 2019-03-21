from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import TrainedStaff


class TrainedStaffSerialiser(serializers.ModelSerializer):
    class Meta:
        model = TrainedStaff
        fields = '__all__'


class TrainedStaffViewSet(ModelViewSet):
    queryset = TrainedStaff.objects.all()
    serializer_class = TrainedStaffSerialiser
    permission_class = [DjangoModelPermissions]


trained_staffRouter = DefaultRouter()
trained_staffRouter.register(r'trained-staff', TrainedStaffViewSet)
