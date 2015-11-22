import random

import datetime
import tmdbsimple
from django.shortcuts import render, redirect
from app.forms import RateForm
from app.models import Movie


def home(request):
    if request.method == 'POST':
        form = RateForm(request)
        id = request.POST["id"]
        movie, created = Movie.objects.get_or_create(tmdb_id=id)
        movie.tmdb_id = id
        if movie.rating_number is None:
            movie.rating_number = 1
            movie.rating = float(request.POST["rating"])
        else:
            movie.rating_number += 1
            movie.rating += (float(request.POST["rating"]) - movie.rating) / movie.rating_number
        movie.title = request.POST["title"]
        movie.save(False, True)
        return redirect("/")
    else:
        popular_movies = tmdbsimple.Movies().popular()
        movie = random.choice(popular_movies["results"])
        trailer = tmdbsimple.Movies(movie['id']).videos()
        trailer_key = trailer["results"][0]["key"]
        date = datetime.datetime.strptime(movie["release_date"], "%Y-%m-%d").strftime("%Y")
        form = RateForm()

    return render(request, "rate.html", locals())
