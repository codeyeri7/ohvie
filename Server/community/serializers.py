from rest_framework import serializers
from .models import Article, Comment, Review, ReviewComment

# 전체 Article 게시판
class ArticleListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ('id', 'userName', 'user', 'title', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('user',)

# 단일 댓글 및 입력
class CommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
        return obj.user.username
    class Meta:
        model = Comment
        fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'article',)
        read_only_fields = ('user','article',)

# 전체 댓글
class CommentListSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=100)
    class Meta:
        model = Comment
        fields = ('content')
        read_only_fields = ('article',)

# 전체 리뷰
class ReviewListSerializer(serializers.ModelSerializer):
  movie_title = serializers.SerializerMethodField()

  def get_movie_title(self, obj):
    return obj.movie.title

  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Review
    fields = ('id', 'user', 'userName', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'movie_title')
    read_only_fields = ('user',)

# 리뷰의 댓글
class ReviewCommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = ReviewComment
        fields = ('id', 'userName', 'user', 'content', 'review', 'rank', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'review',)

