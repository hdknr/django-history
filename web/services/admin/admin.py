from django.contrib import admin
from services import models


@admin.register(models.GoogleKeep)
class GoogleKeepAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.GoogleKeep._meta.fields]

