from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question,Choice
from django.core.urlresolvers import reverse

def index(request):
	last_q = Question.objects.order_by('pub_date')
	context = {'last_q':last_q}
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	q = get_object_or_404(Question,pk=question_id)
	context = {'q':q}
	return render(request,'polls/detail.html', context)

def vote(request,question_id):
	p = get_object_or_404(Question,pk=question_id)
	try:
		sel_choice = p.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'q':p,'error_message':"You didn't select a choice"})
	else:
		sel_choice.votes += 1
		sel_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

def results(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{'q':question})
