from django.contrib import admin
from .models import TypeStorage, StorageUnit, Location

admin.site.register(TypeStorage)
admin.site.register(StorageUnit)
admin.site.register(Location)
