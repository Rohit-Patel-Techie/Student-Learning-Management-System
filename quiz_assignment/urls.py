from django.urls import path
from .views import QuizCreateView, add_question, QuizDetailView, submit_quiz

urlpatterns = [
    path('create/<int:lesson_id>/', QuizCreateView.as_view(), name='quiz-create'),
    path('<int:quiz_id>/add-question/', add_question, name='add-question'),

    path('<int:quiz_id>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('<int:quiz_id>/submit/', submit_quiz, name='submit-quiz'),
]