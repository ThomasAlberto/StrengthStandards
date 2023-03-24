from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkoutForm


def traininglog(request):
    return render(request, "training_log.html")


@login_required
def submit_workout(request):
    form = WorkoutForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('submit-workout')
    return render(request, 'submit_workout.html', {'form': form})


@login_required
def workout_history(request):
    workouts = request.user.workout_set.all().order_by('-date_created')
    return render(request, 'workout_history.html', {'workouts': workouts})

