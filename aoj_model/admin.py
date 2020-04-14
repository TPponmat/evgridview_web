# from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import Aoj_C2

admin.site.register(Aoj_C2, admin.GeoModelAdmin)