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
    path('profile/setting/<pk>/', views.SettingPage.as_view(), name="setting"),

    path("manager/dashboard", views.AdminDashboard.as_view(), name="admin_dashboard"),
    path("manager/job_listing", views.AdminJobListing.as_view(), name="admin_job_listing"),

    # url for manageing degree 
    path('list-degree/', views.DegreeListView.as_view(), name="list-degree"),
    path('create-degree/', views.DegreeCreateView.as_view(), name="create-degree"),
    path('update-degree/<pk>/', views.DegreeUpdateView.as_view(), name="update-degree"),
    path('delete-degree/<pk>/', views.DegreeDeleteView.as_view(), name="delete-degree"),

    # url for manageing major 
    path('list-major/', views.MajorListView.as_view(), name="list-major"),
    path('create-major/', views.MajorCreateView.as_view(), name="create-major"),
    path('update-major/<pk>/', views.MajorUpdateView.as_view(), name="update-major"),
    path('delete-major/<pk>/', views.MajorDeleteView.as_view(), name="delete-major"),

    # url for account removal
    path('list-account-removal-requests/', views.AccountRemovalListView.as_view(), name="list-account-removal-request"),
    path("request-account-removal", views.remove_account_request, name="request-account-removal"),
    path("request-account-removal/<str:pk>/update/", views.update_account_removal_request, name="update-arr-status"),
    ## Request to remove is located on student's profile page

    # url for validator
    path("create-validator", views.create_validator, name="create_validator"),

    # url for managing academic recognition
    path('create-academic-recognition/', views.create_ar, name="create-ar"),
 
]