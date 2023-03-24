from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Exercise(models.Model):
    '''Class Exercise allows us to enter a name and returns it as a string.'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight_lifted = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('workout_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} ({self.weight_lifted} kg, {self.reps} reps)"



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
