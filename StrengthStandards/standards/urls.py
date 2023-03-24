from django.urls import path
from . import views

app_name = "standards"
urlpatterns = [
    path("", views.standards, name="standards"),
    path("bench/", views.bench, name="bench"),
    path("CG-Bench-Press/", views.CGBP, name="close-grip bench-press"),
    path("curl/", views.curl, name="curl"),
    path("deadlift/", views.deadlift, name="deadlift"),
    path("dips/", views.dips, name="dips"),
    path("dumbbell-row/", views.DBRow, name="Dumbbell Row"),
    path("inclineDB/", views.inclineDB, name="Incline Dumbbell Press"),
    path("lateral-raise/", views.lateralRaise, name="Lateral Raise"),
    path("pull-ups/", views.pull_ups, name="Pull Ups"),
    path("pulldown/", views.pulldown, name="Lat Pulldown"),
    path("row/", views.row, name="Barbell row"),
    path("squat/", views.squat, name="Squat"),
    ]
