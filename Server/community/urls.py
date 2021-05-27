from django.urls import path
from . import views

app_name = "community"
urlpatterns = [

    path('articles/', views.article_list_or_create), # 게시글 작성을 위한
    path('detail/<int:article_pk>/', views.article_detail), 
    path('article/<int:article_pk>/', views.article_update_or_delete),

    path('comments/<int:article_pk>', views.comment_list),
    path('<int:article_pk>/comment/', views.create_comment),
    path('comment/<int:article_pk>/<int:comment_pk>/', views.comment_delete),

    
    path('<int:movie_pk>/review_list_create/', views.review_list_or_create), # 리뷰 게시글 작성을 위한
    path('review/<int:review_pk>/', views.review_update_or_delete),

    path('review_comments/<int:review_pk>', views.review_comment_list),
    path('<int:review_pk>/review_comment/', views.create_review_comment),
    path('review_comment/<int:review_pk>/<int:review_comment_pk>/', views.review_comment_delete),
]