from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AnimeTrack


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AddAnimeForm(forms.ModelForm):
    class Meta:
        model = AnimeTrack
        fields = ["title", "description", "episode_count", "watched"]
