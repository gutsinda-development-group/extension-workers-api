from django.db import models
from django_extensions.db.models import TimeStampedModel


class Staff(TimeStampedModel):
    male_staff = models.PositiveIntegerField()
    female_staff = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        db_table = 'staff'
