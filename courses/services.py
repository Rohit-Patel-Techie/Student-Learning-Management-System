#Instructor Courses Fetches
from .models import Course

def get_instructor_courses(user) : 
    return Course.objects.filter(instructor = user)