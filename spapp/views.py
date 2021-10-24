from django.shortcuts import render
from django.views import generic


# Create your views here.

#authentication views
class LoginPage(generic.TemplateView):
  template_name = "authentication/login.html" 

class RegisterPage(generic.TemplateView):
  template_name = "authentication/register.html" 



class JobListingPage(generic.TemplateView):
  template_name = "spapp/job_listing.html"

class TrialPage(generic.TemplateView):
  template_name = "test.html" 

class ProfilePage(generic.TemplateView):
  template_name = "spapp/profile.html" 



# For Manager - Admin - SA

class AdminDashboard(generic.TemplateView):
  template_name = "manager/admin_dashboard.html"

class AdminJobListing(generic.TemplateView):
  template_name = "manager/admin_job_listing.html"


