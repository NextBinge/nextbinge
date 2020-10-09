from django.shortcuts import render
from . import sqlqueries

# Create your views here.
def toprated_view(request):
    context = {'movies': sqlqueries.toprated()}
    return render(request, "searchbase.html", context)

def index(request):
    return render(request, 'index.html')