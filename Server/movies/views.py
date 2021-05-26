from rest_framework.response import Response
# from rest_framework import serializers
from rest_framework.decorators import api_view

from .serializers import MovieSerializer, DetailMovieSerializer
from .models import Movie

from django.shortcuts import get_object_or_404, render
import requests
# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(movies, many=True)
        return Response(movies_serializer.data)

@api_view(['GET'])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    API_KEY = 'f4e4ad237c7fb44ea8e4abb88193fa30'
    URL = (f'https://api.themoviedb.org/3/movie/{movie.movie_id}?api_key={API_KEY}&language=ko-KR')
    response = requests.get(URL)
    data = response.json()
    data = data.get('results')
    movie_serializer = MovieSerializer(movie)
    return Response(movie_serializer.data)
    # return render(request, 'movies/detail.html', data)

