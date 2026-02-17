from django.db import models
from django.utils.text import slugify
from django.conf import settings

#Course Category Table
class Category(models.Model) : 
    name = models.CharField(max_length = 100, unique = True)
    slug = models.SlugField(unique = True)

    def __str__(self) :
        return self.name
    
#Course Name Table
class Course(models.Model) : 
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True, blank = True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to = 'course_thumbnails/')
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'courses')

    category = models.ForeignKey(Category, on_delete = models.PROTECT, related_name = 'courses')

    status = models.CharField(max_length= 20, choices = STATUS_CHOICES, default = 'draft')

    create_at = models.DateTimeField(auto_now_add = True)

    #Save a Slug of Course
    def save(self, *args, **kwargs) : 
        if not self.slug : 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) : 
        return self.title

