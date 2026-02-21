from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import CourseForm, LessonForm
from .models import Course, Category, Lesson
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
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

    def get_course(self) : 
        return get_object_or_404(Course, id = self.kwargs['course_id'], instructor = self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.get_course()
        return context

    def form_valid(self, form) : 
        form.instance.course = self.get_course()
        return super().form_valid(form)

    def get_success_url(self):
        print(self.get_course().slug)
        return reverse('course-detail-view', kwargs = {'slug' : self.get_course().slug})
    
class CourseDetailView(DetailView) : 
    model = Course
    template_name = 'courses/course_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class LessonDetailView(LoginRequiredMixin, DetailView) :
    model = Lesson
    template_name = 'courses/lesson_detail.html'