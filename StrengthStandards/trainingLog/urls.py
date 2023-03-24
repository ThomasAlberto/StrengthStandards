from django.urls import path
from . import views

urlpatterns = [
    path("", views.traininglog, name="Training Logs"),
    path("submit-workout/", views.submit_workout, name='submit-workout'),
    path("workout-history/", views.workout_history, name='workout-history'),
]

