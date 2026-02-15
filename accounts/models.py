from django.db import models
from django.contrib.auth.models import AbstractUser

#Custom User Model
class User(AbstractUser) : 
    STUDENT = "student"
    INSTRUCTOR = "instructor"

    ROLE_CHOICES = [
        (STUDENT, "student"),
        (INSTRUCTOR, "instructor")
    ]

    roles = models.CharField(max_length = 15, choices = ROLE_CHOICES, default = STUDENT)

    def is_student(self) : 
        return self.roles == self.STUDENT
    
    def is_instructor(self) : 
        return self.roles == self.INSTRUCTOR
    
#Student Profile
class StudentProfile(models.Model) : 
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    enrollment_date = models.DateField(auto_now_add = True)

    def __str__(self) : 
        return self.user.username
    
#Instructor Profile
class InstructorProfile(models.Model) : 
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    expertise = models.CharField(max_length = 100, blank = True)

    def __str__(self) : 
        return self.user.username
    

