from django.db import models
from django.conf import settings
from courses.models import Course

# Course Enrollment 
class Enrollment(models.Model) : 
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('cancelled', 'cancelled'),
    )

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'enrollments')
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = 'enrollments')

    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'active' )

    enrolled_at = models.DateTimeField(auto_now_add = True)

    class Meta : 
        constraints = [
            models.UniqueConstraint(
                fields = ['student', 'course'],
                name = 'unique_student_course_enrollment'
            )
        ]

    def __str__(self) : 
        return f"{self.student.user} → {self.course.title}"