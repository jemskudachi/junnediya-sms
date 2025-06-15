from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_number', 'class_name', 'school', 'dob')
    search_fields = ('name', 'roll_number', 'class_name', 'school')
