from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login


# Create your views here.

# this renders the login.html page where you can enter your user and pass
def user_login(request):
    return render(request, 'login.html')


# this is the backend logic that logs someone in
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('login:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('login:show_user')
        )


# this takes us to the final page which tells us the encrypted password and successful login message
def show_user(request):
    print(request.user.username)
    return render(request, 'authenticate_user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
