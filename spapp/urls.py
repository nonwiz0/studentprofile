from django.urls import path
from . import views

app_name = "spapp"
urlpatterns = [
    path('job_listing', views.JobListingPage.as_view(), name="job_listing"),
    path('test', views.TrialPage.as_view(), name="test"),
    path('login', views.LoginPage.as_view(), name="login"),
    path('register', views.RegisterPage.as_view(), name="register"),
    path('', views.ProfilePage.as_view(), name="profile"),

    path("manager/dashboard", views.AdminDashboard.as_view(), name="admin_dashboard"),
    path("manager/job_listing", views.AdminJobListing.as_view(), name="admin_job_listing")

]