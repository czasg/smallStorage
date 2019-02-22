from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
	path('result/', views.result, name='result'),
	path('question/', views.question, name='question'),
	path('vote/', views.vote, name='vote'),
	path('vote_func/', views.vote_func, name='vote_func'),
]
