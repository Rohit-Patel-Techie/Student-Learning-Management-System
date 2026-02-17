from django.contrib import admin
from .models import Course

@admin.register(Course) 
class CourseAdmin(admin.ModelAdmin) : 
    list_display = ('title', 'instructor', 'status', 'create_at')
    list_filter = ('status', 'category')
    prepopulated_fields = {'slug' : ('title',)}