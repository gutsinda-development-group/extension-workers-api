from django.db import models
from django_extensions.db.models import TimeStampedModel


class Experience(TimeStampedModel):
    workStatus = models.CharField(max_length=20)
    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"
        db_table = 'experience'

    def __str__(self):
        return self.workStatus
