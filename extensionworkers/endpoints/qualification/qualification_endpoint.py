from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import Qualification


class QualificationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'


class QualificationViewSet(ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerialiser
    permission_class = [DjangoModelPermissions]


qualificationRouter = DefaultRouter()
qualificationRouter.register(r'qualifications', QualificationViewSet)
