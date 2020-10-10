import requests

def getImage(name):
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=7346d90da037566a43b6a0414c77ea40&query={name}')
    querydata = response.json()
    if querydata != "Nothing Found.":
        imageurl = f'http://image.tmdb.org/t/p/w500{querydata["results"][0]["poster_path"]}'
        return imageurl
    else:
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=7346d90da037566a43b6a0414c77ea40&query=interstellar')
        querydata = response.json()
        imageurl = f'http://image.tmdb.org/t/p/w500{querydata["results"][0]["poster_path"]}'
        return imageurl