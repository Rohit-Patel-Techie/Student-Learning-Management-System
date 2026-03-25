from .models import LessonProgress

def get_course_progress(course, user) : 
    total_lesson = course.lessons.count()

    completed_lesson = LessonProgress.objects.filter(
        student = user, 
        lesson__course = course, 
        completed = True
    ).count()

    if total_lesson == 0 : 
        return 0
    
    progress = ((completed_lesson / total_lesson) * 100)

    return round(progress,2)

    
