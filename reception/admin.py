from django.contrib import admin
from . import models


@admin.register(models.Tutor)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('tutor_name', 'slug', 'tutor_phone', 'tutor_info')
    search_fields = ('tutor_name',)
    prepopulated_fields = {'slug': ('tutor_name',)}
