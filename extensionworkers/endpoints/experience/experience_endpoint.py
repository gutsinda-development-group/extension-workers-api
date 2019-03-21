from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import Experience


class ExperienceSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerialiser
    permission_class = [DjangoModelPermissions]


experienceRouter = DefaultRouter()
experienceRouter.register(r'work-experience', ExperienceViewSet)
