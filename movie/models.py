from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return str(self.movie_id)