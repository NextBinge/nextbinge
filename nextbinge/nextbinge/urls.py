"""nextbinge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from moviedb import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('search/', include('moviedb.urls')),
    path('movie/<int:movie_id>', views.movie_view, name='movie'),
    path('surpriseme/', views.surpriseme, name='surpriseme'),
    path('actor/<int:actor_id>', views.actor_view, name='actor'),
    path('typeahead/', views.typeahead, name='typeahead'),
    path('genre/', views.genre_disp, name='genre'),
    path('genre/<genre_name>/', views.genre_view, name='genre_type'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommend/result', views.result, name='result'),
    path('login/', views.login_view, name='login'),
    path('getresult/', views.getresult, name='getresult'),
    path('newmovie/', views.newmovie, name='newmovie'),
]

