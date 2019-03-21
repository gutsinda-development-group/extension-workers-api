from django.db import models
from django_extensions.db.models import TimeStampedModel


class Qualification(TimeStampedModel):
    FIELD_CHOICES = (
        ('', '[Select Field]'),
        ('Crop', 'Crop'),
        ('Animal Science', 'Animal Science'),
        ('Fisheries', 'Fisheries'),
        ('Forestry', 'Forestry'),
    )
    QUALIFICATION_CHOICES = (
        ('', '[Select Qualification]'),
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),
        ('BSc.', 'BSc.'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
    )
    field = models.CharField(max_length=20, choices=FIELD_CHOICES, null=False)
    qualification = models.CharField(
        max_length=100, choices=QUALIFICATION_CHOICES, null=False)
    isFurtherTraining = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"
        db_table = 'qualification'

    def __str__(self):
        return self.field
