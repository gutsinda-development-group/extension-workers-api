from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import Verifier


class VerifierSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Verifier
        fields = '__all__'


class VerifierViewSet(ModelViewSet):
    queryset = Verifier.objects.all()
    serializer_class = VerifierSerialiser
    permission_class = [DjangoModelPermissions]


verifierRouter = DefaultRouter()
verifierRouter.register(r'verifiers', VerifierViewSet)
