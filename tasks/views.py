from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.utils.translation import get_language
from django.utils.translation import gettext as _


# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup (request):
    print(f"Idioma actual: {get_language()}")
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save()
                messages.success(request, _("User created successfully"))
                return HttpResponse(_('User created successfully'))
            except:
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