from django.contrib import admin
from django.urls import path
from moviedb import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('toprated/', views.toprated_view, name='toprated'),
]
