from django.db import models

class Question(models.Model):
	#question data
	question_title = models.CharField(max_length=200)
	question_content = models.CharField(max_length=200)
	question_date = models.DateTimeField('date')

	def __str__(self):
		return self.question_title


class Choice(models.Model):
	#connect to Question database
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	#choice data
	choice_obj = models.CharField(max_length=200)
	choice_num = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_obj
