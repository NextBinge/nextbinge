from django.contrib import admin
from django.urls import path
from .views import toprated_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('toprated/', toprated_view),
]
