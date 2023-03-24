from django.shortcuts import render

# Create your views here.

def standards(request):
    return render(request, 'standards.html')

def bench(request):
    return render(request, "bench.html")

def CGBP(request):
    return render(request, "CG-Bench-Press.html")

def curl(request):
    return render(request, "curl.html")


def deadlift(request):
    return render(request, "deadlift.html")


def dips(request):
    return render(request, "dips.html")


def DBRow(request):
    return render(request, "dumbbell-row.html")

def inclineDB(request):
    return render(request, "inclineDB.html")

def lateralRaise(request):
    return render(request, "lateral-raise.html")


def pull_ups(request):
    return render(request, "pull-ups.html")


def pulldown(request):
    return render(request, "pulldown.html")


def row(request):
    return render(request, "row.html")


def squat(request):
    return render(request, "squat.html")


