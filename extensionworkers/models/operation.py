from django.db import models
from django_extensions.db.models import TimeStampedModel


class Operation(TimeStampedModel):
    BENEFICIARY_CHOICES = (
        ('', '[Select Key Beneficiaries]'),
        ('Farmers', 'Farmers'),
        ('Students', 'Students'),
        ('Field Extension workers', 'Field Extension workers'),
    )
    CATEGORY_CHOICES = (
        ('', '[Select Farmer category]'),
        ('All Farmers', 'All Farmers'),
        ('Rural', 'Rural'),
        ('Peri-Urban', 'Peri-Urban'),
    )
    GENDER_CHOICES = (
        ('', '[Select Farmer gender]'),
        ('All Genders', 'All Genders'),
        ('Women', 'Women'),
        ('Youth', 'Youth'),
    )
    central_districts = models.TextField(blank=True, null=True)
    eastern_districts = models.TextField(blank=True, null=True)
    northern_districts = models.TextField(blank=True, null=True)
    western_districts = models.TextField(blank=True, null=True)

    key_beneficiaries = models.CharField(
        max_length=40, choices=BENEFICIARY_CHOICES)
    farmer_category = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES)
    farmer_gender = models.CharField(
        max_length=30, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = "Operation"
        verbose_name_plural = "Operations"
        db_table = 'operations'

    def __str__(self):
        return self.key_beneficiaries
