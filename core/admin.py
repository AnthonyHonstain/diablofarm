from django.contrib import admin
from .models import FarmGroup, FarmEvent


admin.site.register(FarmGroup)
admin.site.register(FarmEvent)