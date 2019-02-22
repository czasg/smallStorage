from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice
from django.views.decorators.csrf import csrf_exempt,csrf_protect

def index(request):
	question = Question.objects.all()

	return render(request, 'polls/index.html', {'question':question})


def result(request):
	choice = Choice.objects.all()

	return render(request, 'polls/polls_res.html', {'choice':choice})


def question(request):
	question = Question.objects.all()

	return render(request, 'polls/question.html', {'question':question})


def vote(request):
	choice = Choice.objects.all()

	return render(request, 'polls/vote.html', {'choice':choice})

@csrf_exempt
def vote_func(request):
	choice = Choice.objects.get(pk=request.POST['vote'])
	choice.choice_num += 1
	choice.save()

	choice = Choice.objects.all()

	return render(request, 'polls/polls_res.html', {'choice':choice})
