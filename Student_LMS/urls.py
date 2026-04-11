#Project Level URLS
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name = "accounts-app-urls"),
    path('courses/', include('courses.urls'), name = "courses-app-urls"),
    path('enrollments/', include('enrollments.urls'), name = "enrollments-app-urls"),
    path('progress/', include('progress.urls'), name = "progress-lesson-calculation"),
    path('quiz/', include('quiz_assignment.urls'), name = "quiz-assignment-lesson"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)