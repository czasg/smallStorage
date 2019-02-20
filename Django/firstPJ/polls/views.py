from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader #在HttpResponse中需要进行引用模板是使用的，一旦使用了render其实可以不用导入
from django.urls import reverse

def index(request):
	cza = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	#output = ','.join([q.question_text for q in latest_question_list])
	return render(request, 'polls/index.html', {'cza':cza})
	#return HttpResponse(template.render(context, request)) #和上面等效的把
	#return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
	#try:
	#	question = Question.object.get(pk=question_id)
	#except Question.DoseNotExist:
	#	raise Http404('Question does not exist')
	question = get_object_or_404(Question, pk=question_id)
	#print(question)
	return render(request, 'polls/deatil.html', {'question':question})
	#return HttpResponse('You are looking at questioon %s' % question_id)

def results(request, question_id):
	response = '<h1>You are looking at the results of question %s.</h1>'
	return HttpResponse(response % question_id)

def vote(request, question_id):
	#question = Question.objects.order_by('-pub_date')[:5]
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/deatil.html', {
			'question':question,
			'error_message':'You did not select a choice',
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	#return HttpResponse('You are voting on question %s' % question_id)

