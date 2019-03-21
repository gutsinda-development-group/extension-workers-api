from django.db import models
from django_extensions.db.models import TimeStampedModel

from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import User

from extensionworkers.models.sector import Sector
from extensionworkers.models.staff import Staff
from extensionworkers.models.trained_staff import TrainedStaff
from extensionworkers.models.operation import Operation
from extensionworkers.models.verifier import Verifier


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profiles/organizations/user_{0}/{1}'.format(instance.user.id, filename)


class Organization(TimeStampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        primary_key=True
    )
    institution = models.CharField(max_length=100)
    registrationDate = models.DateField(blank=True, null=True)
    legalRegistrationEntityNo = models.CharField(max_length=30)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    postalAddress = models.TextField()
    district = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    profile_picture = models.FileField(upload_to=user_directory_path)
    sector = models.ForeignKey(
        Sector, on_delete=models.CASCADE)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE)
    trained_staff = models.ForeignKey(
        TrainedStaff, on_delete=models.CASCADE)
    operation = models.ForeignKey(
        Operation, on_delete=models.CASCADE)
    verifier = models.ForeignKey(
        Verifier, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        db_table = 'organization'

    def __str__(self):
        return self.institution
