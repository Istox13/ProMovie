from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('movie', views.get_film),
]
