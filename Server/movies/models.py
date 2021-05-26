from django.db import models
from django.conf import settings
# class 
# 모델 설계 순서:
# 1. popular movies 를 json 형태로 우선 db에 넣어주고
# 2. 선택된 movie에 따라 recommend api에 호출해 return 받아
# 3. 808 get

class Movie(models.Model):
    adult = models.CharField(max_length=10)
    # genre_ids = models.IntegerField()
    # id = models.IntegerField()
    movie_id = models.IntegerField()
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=100)
    overview = models.CharField(max_length=100)
    popularity = models.IntegerField()
    poster_path = models.CharField(max_length=100)
    release_date = models.TextField()
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    recommend = models.CharField(max_length=100)
    book_link = models.CharField(max_length=300)
    book_title = models.CharField(max_length=100)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
