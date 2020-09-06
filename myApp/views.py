from django.shortcuts import render
from . import models
from datetime import datetime
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

temp = id_ = 100000000
found = False


def total_fetch():
    req = Request('https://www.worldometers.info/coronavirus/', headers={'User-Agent': 'Mozilla/5.0'})
    lst = []
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    tags = soup('div')
    for tag in tags:
        if tag.has_attr('id') and tag['id'] == 'maincounter-wrap':
            tds = tag.find_all('div')
            for td in tds:
                lst.append(td.text)
    return lst, webpage


# web scrapping
def fetch(target, webpage):
    global found, id_, temp
    param = []
    soup = BeautifulSoup(webpage, 'html.parser')
    tags = soup('tr')
    for tag in tags:
        if tag.has_attr('style') and tag['style'] == '':
            tds = tag.find_all('td')
            for td in tds:
                if td.text == str(id_ + 1):
                    found = False
                    id_ = 10000000000
                    return param
                if found:
                    param.append(td.text)
                if target == td.text:
                    id_ = int(temp.text)
                    found = True
                temp = td


# Create your views here.
def home(request):
    lst, webpage = total_fetch()
    front_end_parameter_ = {
        'total_case': lst[0],
        'total_death': lst[1],
        'total_recovered': lst[2],
    }
    return render(request, "base.html", front_end_parameter_)


def search_page(request):
    lst, webpage = total_fetch()
    front_end_parameter = {
        'total_case': lst[0],
        'total_death': lst[1],
        'total_recovered': lst[2],
    }
    if request.method == "POST":  # if the search is placed
        search = request.POST.get('search')  # fetching the search bar data
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # capture the date of the current day
        models.Search.objects.create(search_str=search, created=date)
        result = fetch(search, webpage)
        front_end_parameter.update([
            ('continent', result[13]),
            ('search_population', result[12]),
            ('total_count', 616511651),
            ('search', search),
            ('search_total_case', result[0]),
            ('search_new_case', result[1]),
            ('search_total_death', result[2]),
            ('search_new_death', result[3]),
            ('search_total_recovered', result[4]),
            ('search_active_cases', result[6]),
            ('search_serious_critical', result[7]),
            ('search_cases_per_1M', result[8]),
            ('search_death_per_1M', result[9]),
            ('search_total_tests', result[10]),
            ('search_total_tests_per_1M', result[11]),
        ])
    return render(request, "myApp/search.html", front_end_parameter)
