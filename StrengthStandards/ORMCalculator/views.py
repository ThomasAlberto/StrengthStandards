from django.shortcuts import render
from .calculator import calculate_one_rep_max

# Create your views here.

def OneRepMaxCalculator(request):
    return render(request, 'One_Rep_Max.html')


def one_rep_max(request):
    one_rep_max_value = None
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        reps = int(request.POST.get('repetitions'))
        one_rep_max_value = calculate_one_rep_max(weight, reps)

    return render(request, 'one_rep_max_result.html', {'one_rep_max': one_rep_max_value})
