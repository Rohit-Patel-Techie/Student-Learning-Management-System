from django import forms
from django.forms import ModelForm
from .models import Course, Lesson

#Course Form
class CourseForm(forms.ModelForm) : 
    class Meta : 
        model = Course
        fields = ['title', 'description', 'thumbnail', 'category']

#Lesson Form
class LessonForm(forms.ModelForm) : 
    class Meta : 
        model = Lesson
        fields = ['title', 'content', 'order']
