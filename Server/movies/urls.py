from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index),
    # path('<int:movie_id>/', views.detail, name="detail"),

    path('<int:my_pk>/<movie_title>/like/', views.movie_like),
    path('<int:my_pk>/like/', views.my_movie_like),
    path('<int:my_pk>/like/users/', views.like_movie_users),
]