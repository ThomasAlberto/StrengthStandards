from django.urls import path
from . import views

app_name = "ORMCalculator"
urlpatterns = [
    path("", views.OneRepMaxCalculator, name="One Rep Max Calculator"),
    path("one_rep_max_result/", views.one_rep_max, name='one_rep_max_result'),
    ]
