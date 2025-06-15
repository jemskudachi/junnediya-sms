from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'class_name', 'admission_no', 'academic_year')
    search_fields = ('full_name', 'admission_no', 'class_name')
