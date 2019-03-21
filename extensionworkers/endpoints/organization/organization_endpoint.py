from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import Organization


class OrganizationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerialiser
    permission_class = [DjangoModelPermissions]


organizationRouter = DefaultRouter()
organizationRouter.register(r'organizations', OrganizationViewSet)
