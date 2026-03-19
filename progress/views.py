from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from courses.models import Lesson
from enrollments.models import Enrollment
from progress.models import LessonProgress


@login_required
def mark_lesson_complete(request, lesson_id) : 
    lesson = get_object_or_404(Lesson, id = lesson_id)

    if not Enrollment.objects.filter(
        student = request.user,
        course = lesson.course,
        status = "active"
    ).exists():
        return redirect('') # Will Create futher
    
    progress, created = LessonProgress.objects.get_or_create(
        student = request.user,
        lesson = lesson
    )

    progress.completed = True
    progress.completed_at = timezone.now()
    progress.save()

    return redirect("lesson-detail-view", pk = lesson.pk)
