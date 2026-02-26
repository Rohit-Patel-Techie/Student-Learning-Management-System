from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Enrollment

@login_required
def enroll_course(request, course_id) : 
    course = get_object_or_404(Course, id = course_id, status = 'approved')

    #Prevent instructor from enrolling
    if request.user.is_instructor():
        raise PermissionDenied("Instructor Cannot Enroll.")

    #check duplicate
    enrollment, created = Enrollment.objects.get_or_create(student = request.user, course = course)

    if not created :
        messages.warning(request, "You are already Enrolled.")

    else :
        messages.success(request, "Enrollment Successful!")

    return redirect('course-detail-view', slug = course.slug)

