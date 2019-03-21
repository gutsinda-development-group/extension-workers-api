from django.db import models
from django_extensions.db.models import TimeStampedModel


class TrainedStaff(TimeStampedModel):
    LEVEL_CHOICES = (
        ('', '[Select Level]'),
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),
        ('BSc.', 'BSc.'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
    )
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES)
    maleStaff = models.PositiveIntegerField()
    femaleStaff = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Trained Staff"
        verbose_name_plural = "Trained Staff"
        db_table = 'trained_staff'

    def __str__(self):
        return self.level
