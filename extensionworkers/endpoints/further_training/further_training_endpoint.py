from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import FurtherTraining


class FurtherTrainingSerialiser(serializers.ModelSerializer):
    class Meta:
        model = FurtherTraining
        fields = '__all__'


class FurtherTrainingViewSet(ModelViewSet):
    queryset = FurtherTraining.objects.all()
    serializer_class = FurtherTrainingSerialiser
    permission_class = [DjangoModelPermissions]


further_trainingRouter = DefaultRouter()
further_trainingRouter.register(r'further-training', FurtherTrainingViewSet)
