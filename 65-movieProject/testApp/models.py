from django.db import models

# Create your models here.

class Movie(models.Model):
    RATING =  [tuple([str(x),str(x)]) for x in range(1,11)]

    release_date = models.DateField()
    movie_name = models.CharField(max_length=200)
    hero = models.CharField(max_length=50)
    herione = models.CharField(max_length=50)
    rating = models.CharField(max_length=10, choices=RATING)

    def __str__(self):
        return self.movie_name