from django.urls import path
from .views import CourseCreateView

urlpatterns = [
    path("create-courses/", CourseCreateView.as_view(), name = 'course-creation-view')
]