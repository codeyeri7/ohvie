from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleListSerializer, CommentListSerializer, CommentSerializer
from .models import Article, Comment
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list_or_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleListSerializer(article)
    return Response(serializer.data)


# # views in view
# def article_list(request):
#     articles = Article.objects.all()
#     serializers = ArticleSerializer(articles, many=True)
#     return Response(serializers.data)

# @permission_classes([IsAuthenticated])  # is_loggedin
# def create_article(request):
#     serializer = ArticleSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def comment_list_or_create(request):
#     if request.method == 'POST':
#         create_comment(request)
#     else:
#         comment_list(request)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# # 아직 미완성
# @api_view(['PUT', 'DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def article_update_delete(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     if not request.user.articles 
