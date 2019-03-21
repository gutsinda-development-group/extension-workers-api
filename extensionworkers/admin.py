from django.contrib import admin

from .models import (Individual,
                     Organization,
                     Qualification,
                     FurtherTraining,
                     Staff,
                     Sector,
                     TrainedStaff,
                     Operation,
                     Verifier)

admin.site.register(Individual)
admin.site.register(Organization)
admin.site.register(Qualification)
admin.site.register(FurtherTraining)
admin.site.register(Staff)
admin.site.register(Sector)
admin.site.register(TrainedStaff)
admin.site.register(Operation)
admin.site.register(Verifier)

admin.site.site_header = 'MAAIF Extension workers'
