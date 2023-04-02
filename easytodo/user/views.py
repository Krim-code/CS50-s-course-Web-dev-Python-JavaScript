from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .form import NewUserForm


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "user/user.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'user/login.html', {
                "message": "Invalid username or password"
            })
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'user/login.html', {
        "message": "Logged out"
    })


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request,"user/register.html", {"register_form": form})
