from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('article/<int:article_id>/edit/', views.article_edit, name='article_edit'),
    path('article/edit/action', views.article_edit_action, name='article_edit_action'),
    path('article/article_manage/', views.article_manage, name='article_manage'),
    path('article/article_manage/action/', views.article_manage_action, name='article_manage_action'),
    path('article/article/<int:article_id>/comment_manage/', views.comment_manage, name='comment_manage'),
]