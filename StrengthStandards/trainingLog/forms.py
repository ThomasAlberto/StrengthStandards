from django import forms
from .models import Exercise, Workout

class WorkoutForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    weight_lifted = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight (kg)', 'min': 0}))
    reps = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Reps', 'min': 0}))

    class Meta:
        model = Workout
        fields = ('exercise', 'weight_lifted', 'reps')