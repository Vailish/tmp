from django.db import models

# Create your models here.
class Movie(models.Model):
    audlt = models.BooleanField()
    backdrop_path = models.CharField(max_length=200)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    runtime = models.IntegerField()
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
