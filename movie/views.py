from django.shortcuts import render, redirect
from requests import get

# Create your views here.
def index(request, id):
    url = f"http://moonwalk.cc/api/videos.json?kinopoisk_id={id}&api_token=6eb82f15e2d7c6cbb2fdcebd05a197a2"
    film = get(url).json()[0]
    return render(request, "page_film.html", context={"film": film})

def main(request):
    if request.POST:
        return redirect(f"movie/{request.POST['search']}")
    return render(request, "main.html")