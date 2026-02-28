from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/enroll/', views.enroll_course, name = "course-enroll"),
]