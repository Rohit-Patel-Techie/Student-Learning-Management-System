from django.shortcuts import render
from django.urls import reverse
from .forms import CourseForm
from .models import Course, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from accounts.mixins import InstructorRequiredMixin

#Course Creation View
class CourseCreateView(LoginRequiredMixin, InstructorRequiredMixin, CreateView) : 
    model = Course
    form_class = CourseForm

    template_name = 'courses/course_create.html'
    
    def form_valid(self, form):
        form.instance.instructor = self.request.user
        form.instance.status = 'pending'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('instructor-dashboard')
