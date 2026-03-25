from django.urls import path
from .views import mark_lesson_complete

urlpatterns = [
    path("lesson/<int:lesson_id>/complete/", mark_lesson_complete, name = 'mark-lesson-complete'),
]