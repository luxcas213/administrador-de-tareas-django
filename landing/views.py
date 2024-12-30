from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'GET':
        return render(request, 'signup.html',{"form":UserCreationForm()})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                messages.error(request, "Username already exists")
        else:
            messages.error(request, "Invalid data")
        return render(request, 'signup.html', {"form": form})
        
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='GET':
        return render(request, 'login.html',{"form":AuthenticationForm()})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
            return render(request, 'login.html', {"form": form})
        

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')
    