from django.shortcuts import render, redirect
from .calculator import calculate_wilks_results

# Create your views here.

def WilksCalculatorDisplay(request):
    return render(request, 'Wilks_Calculator_Display.html')



def wilks_results(request):
    wilks_score = None
    if request.method == 'POST':
        squat_weight = float(request.POST.get("squat_weight"))
        bench_weight = float(request.POST.get("bench_weight"))
        deadlift_weight = float(request.POST.get("deadlift_weight"))
        bodyweight = float(request.POST.get("bodyweight"))

        wilks_score = calculate_wilks_results(squat_weight, bench_weight, deadlift_weight, bodyweight)

    return render(request, 'wilks_results.html', {'wilks_results': wilks_score})


