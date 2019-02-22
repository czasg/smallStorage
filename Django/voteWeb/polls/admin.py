from django.contrib import admin
from .models import Question,Choice

class QuestionList(admin.ModelAdmin):
	list_display = ('question_title', 'question_date')

class ChoiceList(admin.ModelAdmin):
	list_display = ('choice_obj', 'choice_num')

admin.site.register(Question, QuestionList)
admin.site.register(Choice, ChoiceList)
