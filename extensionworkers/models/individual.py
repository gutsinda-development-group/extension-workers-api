from django.db import models
from django_extensions.db.models import TimeStampedModel

from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import User
from extensionworkers.models.qualification import Qualification
from extensionworkers.models.sector import Sector
from extensionworkers.models.further_training import FurtherTraining
from extensionworkers.models.operation import Operation
from extensionworkers.models.verifier import Verifier


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profiles/individuals/user_{0}/{1}'.format(instance.user.id, filename)


class Individual(TimeStampedModel):
    GENDER_CHOICES = (
        ('', '[Select Gender]'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        primary_key=True
    )
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=6, choices=GENDER_CHOICES, null=False)
    dob = models.DateField(blank=True, null=True)
    nin = models.CharField(max_length=20)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    postalAddress = models.TextField()
    physicalAddress = models.TextField()
    profile_picture = models.FileField(upload_to=user_directory_path)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    sector = models.ForeignKey(
        Sector, on_delete=models.CASCADE)
    operation = models.ForeignKey(
        Operation, on_delete=models.CASCADE)
    verifier = models.ForeignKey(
        Verifier, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Individual"
        verbose_name_plural = "Individual"
        db_table = 'individual'

    def __str__(self):
        return '%s %s' % (self.firstname, self.surname)
