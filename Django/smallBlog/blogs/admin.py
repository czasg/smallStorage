from django.contrib import admin
from .models import Article,Comment

class Article_Display(admin.ModelAdmin):
	list_display = ('article_title', 'article_date')

class Comment_Display(admin.ModelAdmin):
	list_display = ()

admin.site.register(Article, Article_Display)
admin.site.register(Comment, )
