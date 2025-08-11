from django.contrib import admin
from .models import Project

@admin.register(Project)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'image')