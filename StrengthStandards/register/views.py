from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# this renders the page where you can enter the user and pass you want to register
def register(request):
    return render(request, 'register.html')



# this is the backend logic that registers the user
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('register:user_registered')
    else:
        form = UserCreationForm()


    return render(request, 'user_registered.html', {'form': form})



# this renders the page displaying a successful registration message

def user_registered(request):
    username = request.user.username
    password = request.user.password
    return render(request, 'user_registered.html', {'username': username, 'password': password})

