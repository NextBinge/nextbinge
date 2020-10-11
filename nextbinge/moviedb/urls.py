from django.contrib import admin
from django.urls import path
from moviedb import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('toprated/', views.toprated_view, name='toprated'),
    path('mostpopular/', views.mostpopular_view, name='mostpopular'),
    path('recent/', views.recent_view, name='recent'),
    path('toprated/movie/<name>', views.movie_view, name='tratemovie'),
    path('mostpopular/movie/<name>', views.movie_view, name='mpopmovie'),
    path('recent/movie/<name>', views.movie_view, name='recentmovie'),
]
