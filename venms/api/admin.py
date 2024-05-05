from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Vendor)
admin.site.register(models.PO)
admin.site.register(models.HistPerformance)
