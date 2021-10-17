from django.urls import path
from . import views

app_name = "htmx"
urlpatterns = [
    path('create-book/<pk>/', views.create_book, name="create-book"),
    path('', views.my_view, name="home"),
]
