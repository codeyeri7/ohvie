
import re
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from rest_framework import status

from .models import Movie, Article, Comment, Review, ReviewComment
from .serializers import ArticleListSerializer, CommentSerializer, ReviewListSerializer, ReviewCommentSerializer
from community import serializers

# article
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


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if not request.user.articles.filter(pk=article_pk).exists():
        return Response({'message': '접근 권한이 없습니다.'})
    if request.method == 'PUT':
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
    else:
        article.delete()
        return Response({'id': article_pk})


# comment
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
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


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.get(pk=comment_pk)
    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'message': '접근 권한이 없습니다.'})
    else:
        comments.delete()
        return Response({'id': comment_pk})


# review
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_or_create(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.all().filter(movie_id=movie_pk)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = get_object_or_404(Movie, pk=request.data.get('movie'))
            pre_point = movie.vote_average * movie.vote_count
            pre_count = movie.vote_count
            point = pre_point+request.data.get('rank')
            count = movie.vote_count + 1
            new_vote_average = round(point/count, 2)

            movie.vote_average = new_vote_average
            movie.vote_count = count
            movie.save()

            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.reviewcomment_set.all()
    serializer = ReviewCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'message': '접근 권한이 없습니다.'})
    if request.method == 'PUT':
        serializer = ReviewListSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = get_object_or_404(Movie, pk=request.data.get('movie'))
            pre_point = movie.vote_average*(movie.vote_count - 1)
            pre_count = movie.vote_count - 1
            point = pre_point+request.data.get('rank')
            count = movie.vote_count
            new_vote_average = round(point/count, 2)
            movie.vote_average = new_vote_average
            movie.vote_count = count
            movie.save()
            serializer.save(user=request.user)
            return Response(serializer.data)
    else:
        review = get_object_or_404(Review, pk=review_pk)
        movie = get_object_or_404(Movie, pk=review.movie_id)
        pre_point = movie.vote_average * (movie.vote_count)
        pre_count = movie.vote_count
        point = pre_point - review.rank
        count = movie.vote_count - 1
        new_vote_average = round(point/count, 2)
        movie.vote_average = new_vote_average
        movie.vote_count = count
        movie.save()
        review.delete()
        return Response({'id': review_pk})


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_delete(request, review_pk, review_comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = review.reviewcomment_set.get(pk=review_comment_pk)
    if not request.user.review_comments.filter(pk=review_comment_pk).exists():
        return Response({'message': '접근 권한이 없습니다.'})
    else:
        comment.delete()
        return Response({'id': review_comment_pk})

