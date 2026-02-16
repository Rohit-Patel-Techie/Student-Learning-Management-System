from django import forms
from django.forms import ModelForm
from .models import Course

#Course Form
class CourseForm(forms.ModelForm) : 
    class Meta : 
        model = Course
        fields = ['title', 'description', 'thumbnail', 'category']
