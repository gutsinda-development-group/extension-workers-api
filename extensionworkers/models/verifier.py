from django.db import models
from django_extensions.db.models import TimeStampedModel


class Verifier(TimeStampedModel):

    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    institution = models.CharField(max_length=100)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Verifier"
        verbose_name_plural = "Verifiers"
        db_table = 'verifier'

    def __str__(self):
        return '%s %s' % (self.firstname, self.surname)
