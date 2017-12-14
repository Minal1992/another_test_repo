# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projet_name', 'start_date', 'end_date')
    search_fields = ['projet_name']

# Register your models here.
admin.site.register(Project, ProjectAdmin)
