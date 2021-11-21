from django.contrib import admin
from . import models


@admin.register(models.Tutor)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('tutor_name', 'slug', 'tutor_phone', 'tutor_info')
    search_fields = ('tutor_name',)
    prepopulated_fields = {'slug': ('tutor_name',)}


@admin.register(models.Reception)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('reception_date_time', 'tutor')
    list_filter = ('reception_date_time', 'tutor')
    search_fields = ('reception_date_time', 'tutor')
