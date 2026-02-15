#Accounts App URLS
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name = "signup-view"),
    path('login/', views.RoleBasedLoginView.as_view(), name = "login"),
    path('student-dashboard', views.StudentDashboardView.as_view(), name = "student-dashboard"),
    path('instructor-dashboard', views.InstructorDashboardView.as_view(), name = "instructor-dashboard"),
    path('logout', auth_views.LogoutView.as_view(), name = "logout"),

]