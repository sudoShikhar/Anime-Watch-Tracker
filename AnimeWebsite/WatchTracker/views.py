from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm as RegistrationForm
from .forms import RegistrationForm


@login_required(login_url="/watchTracker/login")
def home(request):
    return render(request, "home.html")


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/watchTracker")
        else:
            print("Invalid form")
            return redirect("/watchTracker/sign-up")
    else:
        return render(
            request, "registration/sign_up.html", {"form": RegistrationForm()}
        )
