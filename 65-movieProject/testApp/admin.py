from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = (
        'movie_name',
        'hero',
        'herione',
        'release_date'
    )
