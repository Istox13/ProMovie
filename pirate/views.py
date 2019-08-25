from django.shortcuts import render
from . import keys
from requests import get

def index(request):
    return render(request, 'index.html', context={'info':request.META["REMOTE_ADDR"] })

def get_film(request):
    if True:
        json = get(f"http://moonwalk.cc/api/videos.json?kinopoisk_id={request.GET['id']}&api_token=6eb82f15e2d7c6cbb2fdcebd05a197a2").json()
        if type(json) == list:

            for i in json:
                if i.get("material_data"):
                    return render(request, "page_film.html", context={'film':i})
            else:
                return "Error #404"
        else:
            return render(request, "index.html")
    else:
        return "Error #405"




























