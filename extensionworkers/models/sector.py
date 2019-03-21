from django.db import models
from django_extensions.db.models import TimeStampedModel


class Sector(TimeStampedModel):
    SECTOR_CHOICES = (
        ('', '[Select sector]'),
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Academia', 'Academia'),
        ('NGO', 'NGO'),
        ('Farmers Organization ', 'Farmers Organization '),
    )
    AGRIC_CHOICES = (
        ('', '[Select option]'),
        ('General', 'General'),
        ('Specific', 'Specific'),
    )
    ANIMAL_CHOICES = (
        ('', '[Select option]'),
        ('All', 'All'),
        ('Large livestock(cattle)', 'Large livestock(cattle)'),
        ('small livestock(Sheep, goats', 'small livestock(Sheep, goats'),
        ('Micro livestock(Rabbits)  ', 'Micro livestock(Rabbits)  '),
        ('Birds(Chicken, Turkeys, ducks)', 'Birds(Chicken, Turkeys, ducks)'),
        ('Bees', 'Bees'),
        ('Fisheries', 'Fisheries'),

    )

    CROP_CHOICES = (
        ('', '[Select option]'),
        ('All', 'All'),
        ('Traditional cash crops ( tea, cocoa, coffee, sugarcanes)',
         'Traditional cash crops ( tea, cocoa, coffee, sugarcanes)'),
        ('Cereals and legumes (maize, rice, sorghum, beans, soya, cowpeas, etc)',
         'Cereals and legumes (maize, rice, sorghum, beans, soya, cowpeas, etc)'),
        ('Bananas', 'Bananas'),
        ('Fruits and Vegetables', 'Fruits and Vegetables'),
        ('Commercial Trees', 'Commercial Trees'),
    )

    sector = models.CharField(max_length=40, choices=SECTOR_CHOICES,
                              null=False)
    agricultural_sector_focus = models.CharField(max_length=20,
                                                 choices=AGRIC_CHOICES,
                                                 null=False)
    animal_production = models.CharField(max_length=100,
                                         choices=ANIMAL_CHOICES,
                                         null=True)
    crop_production = models.CharField(max_length=200,
                                       choices=CROP_CHOICES,
                                       null=True)
    post_harvest_handling = models.BooleanField(default=False)
    agribusiness_devt_services = models.BooleanField(default=False)
    consultancy = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"
        db_table = 'sector'

    def __str__(self):
        return self.sector
