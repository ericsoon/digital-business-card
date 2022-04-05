import re
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from templates.form import createuserform
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def inbox(request):
    return render(request, 'inbox.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('inbox')
        else:
            messages.info(request, 'Username or Passowrd is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created from ' + user)
            return redirect('login')
    else:
        form = createuserform()

    return render(request, 'signUp.html', {'form':form})