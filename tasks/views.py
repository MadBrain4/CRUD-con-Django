from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import get_language
from django.utils.translation import gettext as _
from django.db import IntegrityError


# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup (request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save()
                messages.success(request, _("User created successfully"))
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                messages.error(request, _("Username already exists"))
                return redirect('register')
        else:
            messages.error(request, _("Passwords do not match"))
            return redirect('register')
    else:
        return render(request, 'auth/signup.html', {
            'form': UserCreationForm()
        })

def tasks (request):
    return render(request, 'tasks/tasks.html')

def logout_view (request):
    logout(request)
    return redirect('home')

def signin (request):
    print(f"Idioma actual: {get_language()}")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, _("Invalid username or password"))
            return redirect('login')
    else:
        return render(request, 'auth/login.html',
            {'form': AuthenticationForm()
        })
