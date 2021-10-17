from django.urls import path
from . import views

app_name = "spapp"
urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('login', views.LoginPage.as_view(), name="login"),
    path('register', views.RegisterPage.as_view(), name="register"),
]