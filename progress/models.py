from django.conf import settings
from django.db import models
from courses.models import Lesson

#Lesson Progress Tracking Model
class LessonProgress(models.Model) :

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "lesson_progress" )

    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, related_name = "progress_records")

    completed = models.BooleanField(default = False)
    completed_at = models.DateTimeField(null = True, blank = True)

    class Meta : 
        constraints = [
            models.UniqueConstraint(
                fields = ["student", "lesson"],
                name = "unique_student_lesson_progress"
            )
        ]
    
    def __str__(self) :  
        return f"{self.student.username} - {self.lesson.title}"

