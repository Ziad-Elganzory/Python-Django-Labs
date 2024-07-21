from django.shortcuts import render, get_object_or_404
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Movie Series API")


@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        return render(request, 'Pages/index.html', {'movies': movies})

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'GET':
        return render(request, 'Pages/movieDetails.html', {'movie': movie})

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def movies(request):
    movies = Movie.objects.all().prefetch_related('categories', 'casts')
    return render(request, 'Pages/index.html', {'movies': movies})

def movieDetails(request, pk):
    movie = get_object_or_404(Movie.objects.prefetch_related('categories', 'casts'), pk=pk)
    return render(request, 'Pages/movieDetails.html', {'movie': movie})
