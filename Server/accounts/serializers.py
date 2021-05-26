from rest_framework import serializers
# 모델에서 직접 import하면 user model이 변경됬을땐 적용이 안되니까 meta로 상속받게
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        # fields = ('id', 'username', 'password')
        fields = ('id', 'username', 'password', 'avatar',)