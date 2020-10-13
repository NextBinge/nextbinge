from django.shortcuts import render
from . import sqlqueries
from . import poster
from django.http import HttpResponse
import json
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
            'director' : sqlqueries.getnamedirector(movie_id),
            'production_house' : sqlqueries.getnameprod(movie_id),
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

def typeahead(request):
    movies = sqlqueries.getallmovienames()
    return HttpResponse(json.dumps(movies), content_type="application/json")

def search(request):
    if request.method == 'POST':
        searchdict = dict(request.POST.items())
        if(searchdict["searchvalue"] == ""):
            return render(request, 'index.html')
        else:
            searchvalue = searchdict["searchvalue"]
            movieid = sqlqueries.getid(searchvalue)
            context = {'movieid': movieid}
            return render(request, "buffer.html", context)
    else:
        return render(request, 'index.html')

def recommend(request):
    return render(request, 'recommend.html')