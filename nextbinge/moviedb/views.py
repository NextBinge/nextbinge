from django.shortcuts import render
from . import sqlqueries
from . import poster
import random

# Create your views here.
def toprated_view(request):
    context = {'top_rated_movies': sqlqueries.toprated()}
    return render(request, "searchbase.html", context)

def index(request):
    return render(request, 'index.html')

def mostpopular_view(request):
    context = {'most_popular_movies': sqlqueries.mostpopular()}
    return render(request, "searchbase.html", context)

def recent_view(request):
    context = {'recent_movies': sqlqueries.recent()}
    return render(request, "searchbase.html", context)

def movie_view(request, movie_id):
    movie_name = sqlqueries.getname(movie_id)
    context = {'act_descp' : sqlqueries.actor_descp(movie_name),
            'name' : movie_name,
            'img' : poster.getImage(movie_name),
            'description' : sqlqueries.movie_descp(movie_name),
            'director' : sqlqueries.getname(movie_name),
            'production_house' : sqlqueries.getname(movie_name),
    }
    return render(request, "movie_detail.html", context)

def surpriseme(request):
    movies = sqlqueries.getMovies()
    movieid = random.randint(0, len(movies)-1)
    context = {'movieid': movies[movieid]}
    return render(request, "buffer.html", context)
    
def actor_view(request, actor_id):
    actor_name = sqlqueries.getnameactor(actor_id)
    context = {
        'act_desc' : sqlqueries.actor_movies(actor_name),
        'name' : actor_name,
    }
    return render(request, "searchbase.html", context)
