from django.urls import path, include
from . import views

urlpatterns = [
    path('movie/<int:id>', views.index),
    path('', views.main)
]
