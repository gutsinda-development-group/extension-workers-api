from django.db import models
from django_extensions.db.models import TimeStampedModel


class FurtherTraining(TimeStampedModel):
    field = models.CharField(max_length=100)
    started = models.DateField()
    finished = models.DateField()

    class Meta:
        verbose_name = "FurtherTraining"
        verbose_name_plural = "FurtherTrainings"
        db_table = 'further_training'

    def __str__(self):
        return self.field
