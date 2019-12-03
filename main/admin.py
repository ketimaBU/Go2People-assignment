from django.contrib import admin
from main.models import RDV


@admin.register(RDV)
class RDVAdmin(admin.ModelAdmin):
    pass