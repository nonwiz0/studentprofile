from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.urls import reverse

# Create your models here.

class Degree(models.Model):
    name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=50)

    """ the __str__ function overides the name of an object and displays it as a string """
    def __str__(self):
        """ the 'f' before the string, allows you to include varibles in your string, which should 
            be inclosed in curly braces {} """
        return f"{self.name}"

class Major(models.Model):
    """ the ForeignKey creates a relatioship between the degree table (parent) and the Major table (child)
        on_delete, will delete the child, if the parent is deleted
    """
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Major: {self.name}, Degree: {self.degree}"

class Emphasis(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Degree: {self.name}, Major: {self.major}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=10, null=True)
    major = models.OneToOneField(Major, on_delete=models.CASCADE, null=True)
    bio_char = models.CharField(max_length=100, null=True)
    interests = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    website = models.CharField(max_length=12, null=True)
    
    def __str__(self):
        return f"student: {self.user}, id: {self.id_number}"

    def get_absolute_url(self):
        return reverse('spapp:setting', kwargs={'pk': self.user.id})

class Validator(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"   {self.name}"
 

class Activities(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    validator = models.OneToOneField(Validator, null=True, on_delete=models.SET_NULL)
    verification_status = models.BooleanField(default = False)
    #approved_by_manager = models.OneToOneField(Manager, on_delete=models.CASCADE)
    rewarded_points = models.IntegerField(default=0)
    
    def __str__(self):
        return f"activity: {self.activity_name}"
    
class AcademicRecognition(models.Model):
    activity = models.OneToOneField(Activities, on_delete=models.CASCADE, related_name="academic_recognition")
    semester = models.CharField(max_length=15)
    gpa = models.FloatField(max_length=3)
   
class CommunityService(models.Model):
    activity = models.OneToOneField(Activities, on_delete=models.CASCADE, related_name="community_service")
    location = models.CharField(max_length=50)
    
    

class Project(models.Model):
    activity = models.OneToOneField(Activities, on_delete=models.CASCADE, related_name="project")
    resonsibility = models.TextField()
    location = models.CharField(max_length=50)


class Research(models.Model):
    activity = models.OneToOneField(Activities, on_delete=models.CASCADE, related_name="research")
    co_author = models.CharField(max_length=100)
    link = models.CharField(max_length=50)
    published_date = models.DateField()
  
    
class Internship(models.Model):
    activity = models.OneToOneField(Activities, on_delete=models.CASCADE, related_name="internship")


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=50) 


class AccountRemovalRequest(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="account_removal_request")
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.first_name}, Requested: {self.date}, Status: {self.status}"

"""

Plan for Backend:
Student:
- updating personal profile
- registering should show the username of the user 
- if forgotten, maybe create a function to return the username with given email address.
- Request to delete personal information
- Request to add activity
- convert student profile to resume or pdf format

Managers (SA):
- Adding Major and Degree: CRUD
- to manage student accounts
- Update students activity request
- Erase studnet's information (profile)
- Generate log when making operation like Major / Verify

Superuser:
1 Superuser > Multiple Manager (Registrar / SA) > Student

Feb:
Wk1: Summary / Database Checking / Planning
Wk2: Registration of user / updating personal profile / if forgotten password will show / request to delete personal info / CRUD major and degree / Student Account
Wk3: requests to add activity
Wk4:

March:
Wk1:
Wk2:
Wk3:
Wk4:

"""