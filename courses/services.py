#Instructor Courses Fetches
from .models import Course

def get_instructor_courses(user) : 
    # print(Course.objects.filter(instructor = user))
    return Course.objects.filter(instructor = user)