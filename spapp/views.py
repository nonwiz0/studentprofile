from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import *
from random import randint
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.contrib import messages


def logout_view(req):
    logout(req)
    return redirect('spapp:login')


def username_exists(username):
    return User.objects.filter(username=username).exists()


class LoginPage(generic.TemplateView):
    template_name = "authentication/login.html"
    dashboard_template = "spapp/dashboard.html"

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
            # Below here is to tell the user about their username
            login(req, user)
            return render(req, self.dashboard_template, {"status": username})
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
        full_name = data['full_name']  # get full name from the submited input
        arr_full_name = full_name.split(" ")
        # retreive first and last name from the full name
        first_name, last_name = arr_full_name[0], arr_full_name[-1]
        username = data['email']

        """ check if the password are the same, if they are not, then return 'wrong password' else continue saving the user """
        if data['password'] != data['password1']:
            return HttpResponse("Wrong Password")
        """ register the user account """
        user = User.objects.create_user(
            username, data['email'], data['password'])
        user.first_name, user.last_name = first_name, last_name
        user.save()
        """ using the registered user add thier information in the student table """
        student = Student(user=user, id_number=data['id_number'])
        student.save()
        """redirect the user to the dashboard after they signup (log them in) """
        user = authenticate(req, username=username, password=data['password'])
        print(student, "is successfully registered!")
        if user is not None:
            login(req, user)
            return redirect('spapp:dashboard')
        return HttpResponse("Sth went wrong.")


# add function to update profile here
# here
# here
# here
""" To ensure that only logged in user can access the pages, we  'LoginRequiredMixin' to make login mandatory before accessing a page
    The login_url just redirect users back to the login page, if they try to acceess other page wihtout being logged in
"""


class DashboardPage(LoginRequiredMixin, generic.TemplateView):
    login_url = 'spapp:login'
    template_name = "spapp/dashboard.html"


class TrialPage(generic.TemplateView):
    template_name = "test.html"


class ProfilePage(LoginRequiredMixin, generic.TemplateView):
    login_url = 'spapp:login'
    template_name = "spapp/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['recogs'] = Activities.objects.filter(
                student=self.request.user.student)
        except:
            print('Not a student!')
        return context


class SettingPage(LoginRequiredMixin, generic.UpdateView):
    login_url = 'spapp:login'
    template_name = "spapp/setting.html"
    form_class = StudentForm

    def get_object(self):
        return get_object_or_404(Student, id=self.kwargs.get('pk'))

# For Manager - Admin - SA


class AdminDashboard(LoginRequiredMixin, generic.TemplateView):
    login_url = 'spapp:login'
    template_name = "manager/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['majors'] = Major.objects.all()
        context['degrees'] = Degree.objects.all()
        context['account_removal_request'] = AccountRemovalRequest.objects.all()
        return context


class AdminJobListing(LoginRequiredMixin, generic.TemplateView):
    login_url = 'spapp:login'
    template_name = "manager/admin_job_listing.html"


# To display list of degrees in list_degree.html
class DegreeListView(LoginRequiredMixin, generic.ListView):
    login_url = 'spapp:list-degree'
    template_name = 'manager/degree/list_degree.html'
    context_object_name = 'degrees'
    model = Degree


# To create degrees in create_degree.html
class DegreeCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = 'spapp:create-degree'
    template_name = 'manager/degree/create_degree.html'
    fields = '__all__'
    model = Degree
    success_url = reverse_lazy('spapp:admin_dashboard')


# To update degrees in update_degree.html
class DegreeUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/'
    template_name = 'manager/degree/update_degree.html'
    fields = '__all__'
    model = Degree
    success_url = reverse_lazy('spapp:admin_dashboard')

    def get_object(self):
        return Degree.objects.get(id=self.kwargs['pk'])


# To delete degrees in delete_degree.html
class DegreeDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'manager/degree/delete_degree.html'
    success_url = reverse_lazy('spapp:admin_dashboard')
    context_object_name = 'degree'
    model = Degree


# To display list of degrees in list_degree.html
class MajorListView(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    template_name = 'manager/major/list_major.html'
    context_object_name = 'majors'
    model = Major


# To create degrees in create_degree.html
class MajorCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = '/'
    template_name = 'manager/major/create_major.html'
    fields = '__all__'
    model = Major
    success_url = reverse_lazy('spapp:admin_dashboard')

# To update degrees in update_degree.html


class MajorUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/'
    template_name = 'manager/major/update_major.html'
    fields = '__all__'
    model = Major
    success_url = reverse_lazy('spapp:admin_dashboard')

    def get_object(self):
        return self.model.objects.get(id=self.kwargs['pk'])


# To delete degrees in delete_degree.html
class MajorDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = '/'
    template_name = 'manager/major/delete_major.html'
    success_url = reverse_lazy('spapp:admin_dashboard')
    model = Major
    context_object_name = 'major'


# to create academic recognition
def create_update_ar(req):
    try:
        activity, status = Activities.objects.get_or_create(
            student=req.user.student, activity_name="Academic Recognition")
        id = req.POST.get('id')
        semester = req.POST.get('semester')
        gpa = req.POST.get('gpa')
        if id:
            AcademicRecognition.objects.update(
                id=id, activity=activity, semester=semester, gpa=gpa)
        else:
            AcademicRecognition.objects.create(
                activity=activity, semester=semester, gpa=gpa)
    except:
        print('Current logged in user is not a student!')
    return redirect('spapp:profile')


# Student request to remove their account
def remove_account_request(req):
    # For the future: we can create a switch to allow student to request and remove the request
    # removal_request = req.user.student.account_removal_request
    removal_request = AccountRemovalRequest.objects.filter(
        student=req.user.student).first()
    print(removal_request)
    if removal_request is not None:
        print("You already requested!")
        return redirect("spapp:profile")
    removal_request = AccountRemovalRequest.objects.create(
        student=req.user.student)
    print("Requesting account Removal successfully")
    return redirect('spapp:profile')


def update_account_removal_request(req, pk):
    # For the future: we can create a switch to allow student to request and remove the request
    # removal_request = req.user.student.account_removal_request
    removal_request = AccountRemovalRequest.objects.filter(pk=pk).first()
    removal_request.status = not removal_request.status
    removal_request.save()
    print("Requesting account Removal successfully")
    return redirect('spapp:dashboard')


# To display list of Account Removal Request
class AccountRemovalListView(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    template_name = 'manager/account_removal_request/list_account_removal_request.html'
    context_object_name = 'account_removal_requests'
    model = AccountRemovalRequest

# Create validator


def return_post_data(post, arr):
    tmp = []
    for item in arr:
        tmp.append(post[item])
    return tmp


def create_validator(req):
    email, phone, name = return_post_data(req.POST, ["email", "phone", "name"])
    exist_validator = Validator.objects.filter(email=email).first()
    if exist_validator:
        print("Validator is already existed!")
        return redirect('spapp:profile')
    new_validator = Validator.objects.create(
        name=name, email=email, phone_number=phone, created_by=req.user)
    print(new_validator)
    return redirect('spapp:profile')
