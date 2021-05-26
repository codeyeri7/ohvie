from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username, passwords와 같은 정보는 이미 구현이 되있으므로 skip하고 profile avatar 추가
    avatar = models.ImageField(upload_to='user', blank=True)
    # pass