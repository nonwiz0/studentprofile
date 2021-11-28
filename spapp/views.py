from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Student
from random import randint
from .forms import StudentForm
from django.shortcuts import get_object_or_404

def logout_view(req):
  logout(req)
  return redirect('spapp:login')

class LoginPage(generic.TemplateView):
  template_name = "authentication/login.html" 
  
  def post(self, req):
    #print("Post request at Login")
    #print("Request: ", req.POST)

    """ getting inputs from the form based on the name specified on the inputs fields 
        POST is used to pass information from the client side to the server
    """
    username, password = req.POST['username'], req.POST['password']

    """ checking if the username and password are correct (based on registered accounts) 
        You can write your own authentication method, but in our case thanks to django we don't 
        need to do that, we can rely on the autheication function they already have (by importing the function, check line 3)

        the authentication checks if the user exists, and also if the password matches the password for that user. if its all correct
        then an object will be stored in user.
    """
    user = authenticate(req, username=username, password=password)
    if user is not None:
      """ (on line 27 we assigned an object to the variable user, and if its not empty we login and redirect them tot he dashboard) """
      #print("User", user, " loggin successfully")
      login(req, user)
      return redirect('spapp:dashboard')
    else:
      #print("User is not found in database")
      """ if login failed we redirect them back to the login page """
      return render(req, self.template_name)
      
class RegisterPage(generic.TemplateView):
  template_name = "authentication/register.html" 

  def post(self, req):
    print("After you click sign up, here is the info available", req.POST)
    """getting input from the form fields using the POST method in the request and store them as a dictionary (key and value)"""
    data = req.POST

    """ generate default username based on the first name of the user + a random number eg: dan kazimoto ===> dan2122
    """
    full_name = data['full_name'] #get full name from the submited input
    arr_name = full_name.lower().split(" ") #separate the full name based on space and store in array, for example 'john doe' => ['john', 'doe']
    arr_full_name = full_name.split(" ")
    first_name, last_name = arr_full_name[0], arr_full_name[-1] #retreive first and last name from the full name
    filler = str(randint(1000, 9999)) #generate a random number from a range of 1000-9999 and convert it into a string
    username = arr_name[0]+filler  #get the first item in the array we created and join it with a number, to create a unique username . eg => john1231
    
    """ check if the password are the same, if they are not, then return 'wrong password' else continue saving the user """
    if data['password'] != data['password1']:
      return HttpResponse("Wrong Password")
    """ register the user account """
    user = User.objects.create_user(username, data['email'], data['password'])
    user.first_name, user.last_name = first_name, last_name
    user.save()
    """ using the registered user add thier information in the student table """
    student = Student(user = user, id_number = data['id_number'])
    student.save()
    """redirect the user to the dashboard after they signup (log them in) """
    user = authenticate(req, username=username, password=data['password'])
    print(student, "is successfully registered!")
    if user is not None:
      login(req, user)
      return redirect('spapp:dashboard')
    return HttpResponse("Sth went wrong.")


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
  
class SettingPage(LoginRequiredMixin,generic.UpdateView):
  login_url = 'spapp:login'
  template_name = "spapp/setting.html" 
  form_class = StudentForm

  def get_object(self):
      return get_object_or_404(Student, id=self.kwargs.get('pk'))



# For Manager - Admin - SA
class AdminDashboard(LoginRequiredMixin,generic.TemplateView):
  login_url = 'spapp:login'
  template_name = "manager/admin_dashboard.html"

class AdminJobListing(LoginRequiredMixin,generic.TemplateView):
  login_url = 'spapp:login'
  template_name = "manager/admin_job_listing.html"


