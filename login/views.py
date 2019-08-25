from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    if request.session.get('name'):
        return redirect(f'/profile/{request.session["id"]}')
    else:
        if not request.POST:
            return render(request, "registration.html")
        else:
            if not models.User.objects.filter(login=request.POST['login']):
                models.User(login=request.POST['login'], password=request.POST['password']).save()
                return render(request, "registration.html", context={'title': request.POST['login']})
                models.User.login = request.POST['login']

            return redirect(f'/profile/{request.session["id"]}')