from django.views.generic import CreateView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Quiz, Question, Answer
from .models import QuizSubmission
from .forms import QuizForm, QuestionForm, AnswerForm
from courses.models import Lesson
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import InstructorRequiredMixin


class QuizCreateView(LoginRequiredMixin, InstructorRequiredMixin, CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quiz/quiz-create-instructor.html'

    def dispatch(self, request, *args, **kwargs):
        self.lesson = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])

        if self.lesson.course.instructor != request.user:
            return redirect('instructor-dashboard')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.lesson = self.lesson
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('add-question', args=[self.object.id])
    
from django.forms import modelformset_factory

# Add Question & Answers
def add_question(request, quiz_id):

    quiz = get_object_or_404(Quiz, id=quiz_id)

    # 🔐 Security
    if quiz.lesson.course.instructor != request.user:
        return redirect('instructor-dashboard')

    AnswerFormSet = modelformset_factory(
        Answer,
        form=AnswerForm,
        extra=4,  # 4 options
        max_num=4
    )

    if request.method == "POST":
        q_form = QuestionForm(request.POST)
        formset = AnswerFormSet(request.POST)

        if q_form.is_valid() and formset.is_valid():
            question = q_form.save(commit=False)
            question.quiz = quiz
            question.save()

            for form in formset:
                if form.cleaned_data:
                    answer = form.save(commit=False)
                    answer.question = question
                    answer.save()

            return redirect('add-question', quiz.id)

    else:
        q_form = QuestionForm()
        formset = AnswerFormSet(queryset=Answer.objects.none())

    return render(request, 'quiz/add_question.html', {
        'quiz': quiz,
        'q_form': q_form,
        'formset': formset
    })

# Quiz Details 
class QuizDetailView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quiz/quiz_detail.html'
    pk_url_kwarg = 'quiz_id'

#Submit Quiz Result
@login_required
def submit_quiz(request, quiz_id):

    quiz = get_object_or_404(Quiz, id=quiz_id)

    # 🔐 Prevent resubmission
    if QuizSubmission.objects.filter(student=request.user, quiz=quiz).exists():
        return HttpResponse("You already attempted this quiz.")

    total = quiz.questions.count()
    correct = 0

    for question in quiz.questions.all():
        selected = request.POST.get(f"question_{question.id}")

        if not selected:
            return HttpResponse("All questions required!")

        correct_answer = question.answers.filter(is_correct=True).first()

        if str(correct_answer.id) == selected:
            correct += 1

    score = (correct / total) * 100

    QuizSubmission.objects.create(
        student=request.user,
        quiz=quiz,
        score=round(score, 2)
    )

    return render(request, 'quiz/result.html', {
        'quiz': quiz,
        'score': round(score, 2),
        'correct': correct,
        'total': total
    })