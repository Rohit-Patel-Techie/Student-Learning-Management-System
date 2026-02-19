from django.urls import path
from .views import CourseCreateView, LessonCreateView

urlpatterns = [
    path("create-courses/", CourseCreateView.as_view(), name = 'course-creation-view'), 
    path('lesson-create/', LessonCreateView.as_view(), name = 'course-lesson-create'),
]