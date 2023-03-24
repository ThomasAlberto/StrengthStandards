from django.urls import path
from . import views

app_name = "register"
urlpatterns = [
    path("", views.register, name="register"),
    path("register_user", views.register_user, name="register_user"),
    path('user_registered', views.user_registered, name='user_registered')
    ]
