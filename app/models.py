from django import db
from django.db import models


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    tmdb_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255, null=True)
    rating = models.FloatField(null=True)
    rating_number = models.IntegerField(null=True)

