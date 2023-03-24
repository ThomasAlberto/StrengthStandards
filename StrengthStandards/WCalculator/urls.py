from django.urls import path
from . import views

app_name = "WCalculator"
urlpatterns = [
    path("", views.WilksCalculatorDisplay, name="Wilks Calculator"),
    path("wilks_results/", views.wilks_results, name='wilks_results'),
    ]
