from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','age','skills']
    list_filter=['skills']
    search_fields=['first_name','last_name','age','skills']
