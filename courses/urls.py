from django.urls import path
from .views import CourseCreateView, LessonCreateView, CourseDetailView, LessonDetailView

urlpatterns = [
    path("create-courses/", CourseCreateView.as_view(), name = 'course-creation-view'), 
    path('lesson-create/', LessonCreateView.as_view(), name = 'course-lesson-create'),
    path('course-detail/<slug:slug>', CourseDetailView.as_view(), name = "course-detail-view"),
    path('lesson-detail/<slug:slug>', LessonDetailView.as_view(), name = "lesson-detail-view"),

]