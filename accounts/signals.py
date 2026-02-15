# Auto Profile Creation Signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, StudentProfile, InstructorProfile

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs) : 
    if created : 
        if instance.roles == User.STUDENT : 
            StudentProfile.objects.create(user = instance)
        
        elif instance.roles == User.INSTRUCTOR : 
            InstructorProfile.objects.create(user = instance)
        
