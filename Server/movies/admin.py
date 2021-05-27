from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Movie

admin.site.register(Movie)