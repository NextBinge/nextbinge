from django.contrib import admin
from django.urls import path
from moviedb import views

urlpatterns = [
    path('', views.search),
    path('admin/', admin.site.urls),
    path('toprated/', views.toprated_view, name='toprated'),
    path('mostpopular/', views.mostpopular_view, name='mostpopular'),
    path('recent/', views.recent_view, name='recent'),
]
