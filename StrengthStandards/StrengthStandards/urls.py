
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("index.urls")),
    path("login/", include("login.urls")),
    path("register/", include("register.urls")),
    path("standards/", include("standards.urls")),
    path("ORMCalculator/", include("ORMCalculator.urls")),
    path("WCalculator/", include("WCalculator.urls")),
    path("trainingLog/", include("trainingLog.urls"))
]
