from django.contrib import admin
from django.urls import path
from moviedb import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('toprated/', views.toprated_view, name='toprated'),
    path('mostpopular/', views.mostpopular_view, name='mostpopular'),
    path('recent/', views.recent_view, name='recent'),
    path('top50/', views.top50_view, name='top50'),
]
