from django.shortcuts import render
from . import models
from datetime import datetime


# Create your views here.
def home(request):
    front_end_parameter = {
        'total_count': 26_475_568,
    }
    return render(request, "base.html", front_end_parameter)


def search_page(request):
    search = request.POST.get('search')  # fetching the search bar data
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # capture the date of the current day
    if request.method == "POST":  # if the search is placed
        models.Search.objects.create(search_str=search, created=date)
    front_end_parameter = {
        'search': search,
        'total_count': 26_475_568,
    }
    return render(request, "myApp/search.html", front_end_parameter)
