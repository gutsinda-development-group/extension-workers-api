from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import Staff


class StaffSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerialiser
    permission_class = [DjangoModelPermissions]


staffRouter = DefaultRouter()
staffRouter.register(r'staff', StaffViewSet)
