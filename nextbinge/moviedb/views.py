from django.shortcuts import render, redirect
from . import sqlqueries
from . import poster
from django.http import HttpResponse, JsonResponse
import json
import random
import ast, csv, itertools, datetime

recom = []

def login_view(request):
    return render(request, "login.html")

# Create your views here.
def toprated_view(request):
    context = {'top_rated_movies': sqlqueries.toprated()}
    return render(request, "searchbase.html", context)

def index(request):
    if request.method == 'POST':
        userinput = dict(request.POST.items())
        print(userinput)
        if userinput["type"] == "delete":
            id=sqlqueries.getid(userinput['moviename'])
            sqlqueries.delete_movie_id_char(id)
            sqlqueries.delete_movie_id_details(id)
            sqlqueries.delete_movie_id(id)
            # print(id)
        else:
            actoridset=[]
            character_name=[]
            castvalues=[]
            movievalues=[]
            charactervalues=[]
            detailsvalues=[]

            genre_arr=userinput['genres']
            character_name=userinput['charactername'].split(",")
            actor_name=userinput['actorname'].split(",")
            movie_name=userinput['moviename']
            movie_max=int((sqlqueries.max_movie()))+1
            cast_max=int((sqlqueries.max_cast()))

            for name in actor_name:
                actoridset.append(sqlqueries.actor_id_retrieve(name))
            directoridset = sqlqueries.director_id_retrieve(userinput["directorname"])
            prodidset = sqlqueries.production_id_retrieve(userinput["productionhouse"])

            for i in range(len(actoridset)):
                cast_max+=1
                castvalues.append((cast_max,actoridset[i], directoridset, prodidset))
                movievalues.append((movie_max, cast_max, movie_name))
            
            detailsvalues.append(movie_max)
            detailsvalues.append(userinput['genres'])
            detailsvalues.append(userinput['description'])
            detailsvalues.append(userinput['runtime'])
            detailsvalues.append(userinput['releasedate'])
            detailsvalues.append(userinput['popularity'])
            detailsvalues.append(userinput['rating'])
            detailsvalues.append('100')

            sqlqueries.insert_into_cast(castvalues)
            sqlqueries.insert_into_movie(movievalues)
            sqlqueries.insert_into_details(detailsvalues)

            for i in range(len(actoridset)):
                charactervalues.append((movie_max,actoridset[i],character_name[i]))

            sqlqueries.insert_into_character(charactervalues)
            # print(castvalues)
            # print(movievalues)
            # print(detailsvalues)
            # print(charactervalues)
    context = {
        'most_popular_movies': sqlqueries.mostpopular(),
        'wrong':0,  
    }
    return render(request, 'index.html', context)

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
            context={'wrong': 1,
                'most_popular_movies': sqlqueries.mostpopular(),
            } #toast movie not available
            return render(request, 'index.html', context)
        else:
            searchvalue = searchdict["searchvalue"]
            movieid = sqlqueries.getid(searchvalue)
            if(movieid != 0):
                context = {'movieid': movieid}
                return render(request, "buffer.html", context)
            else:
                context={'wrong': 1,
                    'most_popular_movies': sqlqueries.mostpopular(),
                } #toast movie not available
                return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def genre_disp(request):
    
    context={
        'action':sqlqueries.getMovies_genre("action"),
        'adventure':sqlqueries.getMovies_genre("adventure"),
        'horror':sqlqueries.getMovies_genre("horror"),
        'sciencefiction':sqlqueries.getMovies_genre("science fiction"),
        'comedy':sqlqueries.getMovies_genre("comedy"),
        'romance':sqlqueries.getMovies_genre("romance"),
        'thriller':sqlqueries.getMovies_genre("thriller"),
        'crime':sqlqueries.getMovies_genre("crime"),
        'scifi': "Interstellar",
    }
    return render(request, "genre.html", context)

def recommend(request):
    return render(request, 'recommend.html')

def result(request):
    idlist = []
    idlist.append(sqlqueries.getid(recom[0]))
    idlist.append(sqlqueries.getid(recom[1]))
    idlist.append(sqlqueries.getid(recom[2]))
    context = {"movies": recom, "id": idlist}
    return render(request, 'recommendresult.html', context)

def getresult(request):
    if request.method == "POST":
        userinput = json.loads(request.body)
        genres = sqlqueries.getGenre(userinput)
        sortedGenres = sorted(set(genres), key = lambda ele: genres.count(ele))
        sortedGenres.reverse()
        allRecommendation = sqlqueries.getRecommendation(sortedGenres)
        sortedRecommendation = sorted(set(allRecommendation), key = lambda ele: allRecommendation.count(ele))
        sortedRecommendation.reverse()
        if userinput[0] in sortedRecommendation:
            sortedRecommendation.remove(userinput[0])
        if userinput[1] in sortedRecommendation:
            sortedRecommendation.remove(userinput[1])
        if userinput[2] in sortedRecommendation:
            sortedRecommendation.remove(userinput[2])
        recom.clear()
        recom.append(sortedRecommendation[0])
        recom.append(sortedRecommendation[1])
        recom.append(sortedRecommendation[2])
        print(recom)
        return JsonResponse({'redirect': 'http://127.0.0.1:8000/recommend/result'})

def genre_view(request, genre_name):
    if genre_name == "sciencefiction":
        genre_name = "science fiction"

    context={
        'genre_movie_detail': sqlqueries.genre_detail(genre_name),
        'name': genre_name,
    }
    return render(request, 'searchbase.html', context)

def newmovie(request):
    username = 'admin123'
    password = 'admin123'
    if request.method == 'POST':
        print(request)
        userinput = dict(request.POST.items())
        print(userinput)
        if userinput["username"] == username and userinput["password"] == password:
            return render(request, 'add_movie.html')
        else:
            context = {
                'most_popular_movies': sqlqueries.mostpopular(),  
            }
            return render(request, 'index.html', context)
