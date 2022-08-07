from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(url="home/")),
    path("home/", views.home, name="WatchTracker Home"),
    path("addAnime/", views.add_anime, name="Add new Anime"),
    # path('deleteAnime/',views.add_new_anime,name='Delete Anime'),
    # path('TrackAnime/',views.add_new_anime,name='Track Anime'),
    path("sign-up/", views.sign_up, name="Sign Up"),
]
