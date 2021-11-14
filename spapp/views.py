from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#authentication views
def logout_view(req):
  logout(req)
  return redirect('spapp:login')

class LoginPage(generic.TemplateView):
  template_name = "authentication/login.html" 
  
  def post(self, req):
    print("Post request at Login")
    print("Request: ", req.POST)

    """ getting inputs from the form based on the name specified on the inputs fields 
        POST is used to pass information from the client side to the server
    """
    username, password = req.POST['username'], req.POST['password']

    """ checking if the username and password are correct (based on registered accounts) 
        You can write your own autheication method, but in our case thanks to django we don't 
        need to do that, we can rely on the autheication function they already have (by importing the function, check line 3)

        the autheication checks if the user exists, and also if the password matches the password for that user. if its all correct
        then an object will be stored in user.
    """
    user = authenticate(req, username=username, password=password)
    if user is not None:
      """ (on line 27 we assigned an object to the variable user, and if its not empty we login and redirect them tot he dashboard) """
      print("User", user, " loggin successfully")
      login(req, user)
      return redirect('spapp:dashboard')
    else:
      print("User is not found in database")
      """ if login failed we redirect them back to the login page """
      return render(req, self.template_name)
      

class RegisterPage(generic.TemplateView):
  template_name = "authentication/register.html" 

""" To ensure that only logged in user can access the pages, we  'LoginRequiredMixin' to make login mandatory before accessing a page
    The login_url just redirect users back to the login page, if they try to acceess other page wihtout being logged in
"""
class DashboardPage(LoginRequiredMixin, generic.TemplateView):
  login_url = 'spapp:login'
  template_name = "spapp/dashboard.html"

class TrialPage(generic.TemplateView):
  template_name = "test.html" 

class ProfilePage(LoginRequiredMixin,generic.TemplateView):
  login_url = 'spapp:login'
  template_name = "spapp/profile.html" 
  
class SettingPage(LoginRequiredMixin,generic.TemplateView):
  login_url = 'spapp:login'
  template_name = "spapp/setting.html" 


# For Manager - Admin - SA
class AdminDashboard(LoginRequiredMixin,generic.TemplateView):
  login_url = 'spapp:login'
  template_name = "manager/admin_dashboard.html"

class AdminJobListing(LoginRequiredMixin,generic.TemplateView):
  login_url = 'spapp:login'
  template_name = "manager/admin_job_listing.html"


