from django.contrib import admin
from django.urls import path
from moviedb import views

urlpatterns = [
    path('', views.search),
    path('admin/', admin.site.urls),
    path('toprated/', views.toprated_view, name='toprated'),
    path('mostpopular/', views.mostpopular_view, name='mostpopular'),
    path('recent/', views.recent_view, name='recent'),
    # path('action/', views.recent_view, name='action'),
    # path('adventure/', views.recent_view, name='adventure'),
    # path('horror/', views.recent_view, name='horror'),
    # path('sciencefiction/', views.recent_view, name='sciencefiction'),
    # path('crime/', views.recent_view, name='crime'),
    # path('comedy/', views.recent_view, name='comedy'),
    # path('romance/', views.recent_view, name='romance'),
    # path('thriller/', views.recent_view, name='thriller'),

]
