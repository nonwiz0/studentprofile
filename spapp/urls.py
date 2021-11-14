from django.urls import path
from . import views

app_name = "spapp"
urlpatterns = [
    path('', views.DashboardPage.as_view(), name="dashboard"),
    path('test', views.TrialPage.as_view(), name="test"),
    path('login', views.LoginPage.as_view(), name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.RegisterPage.as_view(), name="register"),
    path('profile', views.ProfilePage.as_view(), name="profile"),
    path('profile/setting', views.SettingPage.as_view(), name="setting"),

    path("manager/dashboard", views.AdminDashboard.as_view(), name="admin_dashboard"),
    path("manager/job_listing", views.AdminJobListing.as_view(), name="admin_job_listing")

]