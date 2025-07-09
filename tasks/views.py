from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.utils.translation import get_language


# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup (request):
    print(f"Idioma actual: {get_language()}")
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            user.save()
            messages.success(request, "User created successfully")
            return HttpResponse('User created successfully')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'auth/signup.html', {
            'form': UserCreationForm()
        })

