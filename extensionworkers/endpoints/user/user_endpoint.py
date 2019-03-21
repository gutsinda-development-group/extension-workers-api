from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from extensionworkers.models import User


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_individual', 'is_organization')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_class = [DjangoModelPermissions]


userRouter = DefaultRouter()
userRouter.register(r'users', UserViewSet)
