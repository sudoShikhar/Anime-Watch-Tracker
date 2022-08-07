from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm as RegistrationForm
from .forms import RegistrationForm, AddAnimeForm
from .models import AnimeTrack


@login_required(login_url="/watchTracker/login")
def home(request):
    if request.method == "POST":
        anime_id = request.POST.get("delete-post-id")
        anime = AnimeTrack.objects.get(id=anime_id)
        anime.delete()
    anime = AnimeTrack.objects.filter(user=request.user)
    return render(request, "home.html", {"anime": anime})


@login_required(login_url="/watchTracker/login")
def add_anime(request):
    if request.method == "POST":
        form = AddAnimeForm(request.POST)
        if form.is_valid():
            anime_add = form.save(commit=False)
            anime_add.user = request.user
            anime_add.save()
            return redirect("/watchTracker")
    else:
        return render(request, "add_anime.html", {"form": AddAnimeForm()})


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
