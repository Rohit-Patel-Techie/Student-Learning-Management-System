from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import SignupForm
from .utils import get_dashboard_url
from .mixins import StudentRequiredMixin, InstructorRequiredMixin

#Sign View
def signup_view(request) : 
    if request.method == 'POST' : 
        form = SignupForm(request.POST)
        if form.is_valid() : 
            user = form.save()
            print("Coming")
            login(request,user)
            return redirect(get_dashboard_url(user))        
    else : 
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form' : form})

#Login View
class RoleBasedLoginView(LoginView) : 
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse(get_dashboard_url(self.request.user))

#Student Dashboard
class StudentDashboardView(LoginRequiredMixin, StudentRequiredMixin, TemplateView) : 
    template_name = 'accounts/student-dashboard.html'


#Instructor Dashboard
class InstructorDashboardView(LoginRequiredMixin,InstructorRequiredMixin, TemplateView) : 
    template_name = 'accounts/instructor-dashboard.html'

