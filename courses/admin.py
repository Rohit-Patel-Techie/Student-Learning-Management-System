from django.contrib import admin
from .models import Course, Category

@admin.register(Category)
class CourseCategoryAdmin(admin.ModelAdmin) : 
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug' : ('name',)}


@admin.register(Course) 
class CourseAdmin(admin.ModelAdmin) : 
    list_display = ('title', 'instructor', 'status', 'thumbnail', 'create_at')
    list_filter = ('status', 'category')
    prepopulated_fields = {'slug' : ('title',)}