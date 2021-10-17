from django.shortcuts import render
from django.views import generic


# Create your views here.
class Index(generic.TemplateView):
  template_name = "spapp/index.html"

class LoginPage(generic.TemplateView):
  template_name = "authentication/login.html" 

class RegisterPage(generic.TemplateView):
  template_name = "authentication/register.html" 
