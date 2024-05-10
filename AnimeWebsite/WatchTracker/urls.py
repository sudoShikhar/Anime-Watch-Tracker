from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from .forms import UserLoginForm
from . import views


urlpatterns = [
    path("", views.home, name="WatchTracker Home"),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
            ),
        name='WatchTracker Login'
    ),
    path("getTrackedAnime/", views.get_tracked_anime, name="Get Tracked Anime"),
    path("addAnime/", views.add_anime, name="Add new Anime"),
    path("updateAnime/<int:tracking_id>", views.update_anime, name="Update Anime"),
    path('deleteAnime/<int:tracking_id>',views.delete_anime,name='Delete Anime'),
    path("sign-up/", views.sign_up, name="Sign Up"),
]
