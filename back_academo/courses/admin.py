from django.contrib import admin
from .models import Subject, Course, Classes

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']

class ModuleInline(admin.StackedInline):
    model = Classes

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    inlines = [ModuleInline]