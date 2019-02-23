from django.shortcuts import render
from .models import Article,Comment
from django.utils import timezone
from django.http import HttpResponse

def index(request):
	articles = Article.objects.all()
	comments = Comment.objects.all()
	return render(request, 'blogs/index.html', {'articles':articles, 'comments':comments})


def  article(request, article_id):
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	return render(request, 'blogs/article.html', {'article':article, 'comments':comments})


def article_edit(request, article_id):
	if str(article_id) == '0':
		return render(request, 'blogs/article_edit.html')
	else:
		article = Article.objects.get(pk=article_id)
		return render(request, 'blogs/article_edit.html', {'article':article})


def article_edit_action(request):
	article_title = request.POST.get('article_title')
	article_content = request.POST.get('article_content')
	id_hidden = request.POST.get('id_hidden')

	if str(id_hidden) == '0':
		Article.objects.create(article_title=article_title, article_content=article_content, article_date=timezone.now())
		articles = Article.objects.all()
		comments = Comment.objects.all()
		return render(request, 'blogs/index.html', {'articles':articles, 'comments':comments})
	else:
		article = Article.objects.get(pk=id_hidden)
		article.article_title = article_title
		article.article_content = article_content
		article.article_date = timezone.now()
		article.save()
		return render(request, 'blogs/article.html', {'article':article})


def article_manage(request):
	articles = Article.objects.all()
	comments = Comment.objects.all()	
	return render(request, 'blogs/article_manage.html', {'articles':articles, 'comments':comments})

def article_manage_action(request):
	if request.POST.get('type') == '0':
		article_id = request.POST.get('article_id')
		Article.objects.get(pk=article_id).delete()
		articles = Article.objects.all()
		comments = Comment.objects.all()
		return render(request, 'blogs/index.html', {'articles':articles, 'comments':comments})
	elif request.POST.get('type') == '1':
		comment_id = request.POST.get('comment_id')
		Comment.objects.get(pk=comment_id).delete()
		articles = Article.objects.all()
		comments = Comment.objects.all()
		return render(request, 'blogs/index.html', {'articles':articles, 'comments':comments})
	else:
		return 	HttpResponse('ERROR!')


def comment_manage(request, article_id):
	article = Article.objects.get(pk=article_id)
	comment_content = request.POST.get('comment_content')
	article.comment_set.create(comment_content=comment_content, comment_date=timezone.now())
	articles = Article.objects.all()
	comments = Comment.objects.all()
	return render(request, 'blogs/index.html', {'articles':articles, 'comments':comments})

