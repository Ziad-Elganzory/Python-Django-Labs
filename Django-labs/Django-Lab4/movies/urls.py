from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('movies/<int:pk>/', views.movieDetails, name='movieDetails'),
]
