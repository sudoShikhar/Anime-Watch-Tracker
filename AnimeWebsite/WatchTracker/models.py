from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class AnimeTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    episode_count = models.IntegerField(
        blank=False,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )
    watched = models.IntegerField(
        blank=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)],
    )
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            self.title
            + " added by "
            + self.user.username
            + " on "
            + str(self.added_on.strftime("%c"))
            + ". Watched "
            + str(self.watched)
            + "/"
            + str(self.episode_count)
            + "."
        )
