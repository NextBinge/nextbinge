from django.shortcuts import render
from . import sqlqueries
from . import poster

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

def movie_view(request, movie_name):
    context = {'act_descp' : sqlqueries.actor_name(movie_name),
            'name' : movie_name,
            'img' : poster.getImage(movie_name),
            'description' : sqlqueries.movie_descp(movie_name),
    }
    return render(request, "movie_detail.html", context)