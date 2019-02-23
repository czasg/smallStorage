from django.db import models

class Article(models.Model):
	article_title = models.CharField(max_length=200)
	article_content = models.TextField(max_length=256)
	article_date = models.DateTimeField('article_date')

	def __str__(self):
		return self.article_title


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	comment_content = models.CharField(max_length=200)
	comment_date = models.DateTimeField('comment_date')

	def __str__(self):
		return self.comment_content
