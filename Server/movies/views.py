from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer
from .models import Movie

import requests
# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(movies, many=True)
        return Response(movies_serializer.data)

# @api_view(['GET'])
# def detail(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     API_KEY = 'f4e4ad237c7fb44ea8e4abb88193fa30'
#     URL = (f'https://api.themoviedb.org/3/movie/{movie.movie_id}?api_key={API_KEY}&language=ko-KR')
#     response = requests.get(URL)
#     data = response.json()
#     data = data.get('results')
#     movie_serializer = MovieSerializer(movie)
#     return Response(movie_serializer.data)
#     # return render(request, 'movies/detail.html', data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
  else:
      me.like_movies.add(movie.pk)
      liking = True
  return Response(liking)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    return Response(data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie_users(request, my_pk):
    users = []
    movies = request.data.get('movies')
    for movie in movies:
        movie = get_object_or_404(Movie, pk=movie)
        serializer = MovieSerializer(movie)
        for user in serializer.data.get('like_users'):
            if user not in users:
                users.append(user)
        return Response(users)