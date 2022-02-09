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
]