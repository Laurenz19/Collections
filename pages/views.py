from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm
from myCollection.models import *

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for'+ user)
                return redirect('login')

        context = {'form': form }
        return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def error_404(request,exception):
    return render(request, 'apps/404.html')


@login_required(login_url='login')
def homePage(request):
    context = {
        'collections': Collection.objects.all(),
        'series': Collection.objects.filter(Type__title='Serie'),
        'games': Collection.objects.filter(Type__title='jeux'),
        'films': Collection.objects.filter(Type__title='film')
    }
    return render(request, 'apps/home.html', context)
