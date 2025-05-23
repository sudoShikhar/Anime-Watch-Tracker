from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings


from .forms import RegistrationForm, AddAnimeForm
from .models import AnimeTrack


def home(request):
    print(settings.DEPLOYMENT_URLS)
    return render(request, "homepage.html", {
        "user_authenticated": request.user.is_authenticated, 
        **settings.DEPLOYMENT_URLS
    })

@login_required
def get_tracked_anime(request):
    anime = AnimeTrack.objects.filter(user=request.user).all()
    return render(request, "tracked.html", {"anime": anime})

@login_required
def add_anime(request):
    if request.method == "POST":
        form = AddAnimeForm(request.POST)
        if form.is_valid():
            anime_add = form.save(commit=False)
            anime_add.user = request.user
            anime_add.save()
            return redirect(reverse("Get Tracked Anime"))
    else:
        return render(request, "add_anime.html", {"form": AddAnimeForm()})

@login_required
def update_anime(request, tracking_id):
    if request.method == "POST":
        form = AddAnimeForm(request.POST)
        if form.is_valid():
            AnimeTrack.objects.filter(id=tracking_id).update(**form.cleaned_data)
            return redirect(reverse("Get Tracked Anime"))

    anime = AnimeTrack.objects.get(id=tracking_id)
    return render(request, "add_anime.html", {"form": AddAnimeForm(vars(anime)), "update": True})

@login_required
def delete_anime(request, tracking_id):
    anime = AnimeTrack.objects.filter(user=request.user, id=tracking_id)
    anime.delete()
    return redirect(reverse("Get Tracked Anime"))

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("WatchTracker Home"))
        else:
            return render(request, "registration/sign_up.html", {"form": form})
    else:
        return render( request, "registration/sign_up.html", {"form": RegistrationForm()})
