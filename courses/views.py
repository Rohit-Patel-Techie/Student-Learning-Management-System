from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import CourseForm, LessonForm
from .models import Course, Category, Lesson
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
    

class LessonCreateView(LoginRequiredMixin, InstructorRequiredMixin, CreateView) : 
    model = Lesson
    form_class = LessonForm
    template_name = 'courses/lesson_create.html'

    def form_valid(self, form) : 
        course = get_object_or_404(Course, id = self.kwargs['course_id'], instructor = self.request.user)
        form.instance.course = course
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('instructor-dashboard')