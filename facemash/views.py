from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from facemash.models import User
from django.core.urlresolvers import reverse
import random
import sys
import json

def index(request):
	return render(request,'facemash/index.html',{})

def choose(request,gender):
	u_list = User.objects.filter(user_gender=gender).order_by('user_rating')
	n=0
	m=0
	while n == m:
		n = random.randint(0,len(u_list)-1)
		m = random.randint(0,len(u_list)-1)
	user_A = u_list[n]
	user_B = u_list[m]
	# if n == 0:
	# 	user_B = u_list[n+1]
	# elif n == len(u_list)-1:
	# 	user_B = u_list[len(u_list-2)]
	# else:
	# 	if abs(user_A.user_rating - u_list[n+1].user_rating) < abs(user_A.user_rating - u_list[n-1].user_rating):
	# 		user_B = u_list[n+1]
	# 	else:
	# 		user_B = u_list[n-1]
	context = {'user_A':user_A,'user_B':user_B,'gender':gender}
	return render(request,'facemash/choose.html',context)


def vote(request,lose_id,win_id):
	if len(lose_id) > 0 and len(win_id) > 0:
		lose_user = get_object_or_404(User,user_id=lose_id) # A
		win_user  = get_object_or_404(User,user_id=win_id)  # B
		old_A = lose_user.user_rating
		old_B = win_user.user_rating
		expected_A = 1/float(1+10**((win_user.user_rating-lose_user.user_rating)/400))
		expected_B = 1-expected_A
		score_A = 0
		score_B = 1
		new_score_A = lose_user.user_rating + 32*(score_A-expected_A)
		new_score_B = win_user.user_rating + 32*(score_B-expected_B)
		lose_user.user_rating = new_score_A
		win_user.user_rating = new_score_B
		lose_user.save()
		win_user.save()
		l = [old_A,new_score_A,expected_A,score_A]
		w = [old_B,new_score_B,expected_B,score_B]
		# print >>sys.stderr, 'Lose: '+str(old_A)+'-->'+str(lose_user.user_rating)
		# print >>sys.stderr, 'Win: '+str(old_B)+'-->'+str(win_user.user_rating)
		print >>sys.stderr,json.dumps(l)
		print >>sys.stderr,json.dumps(w)

		return HttpResponseRedirect(reverse('facemash:choose',args=(win_user.user_gender,)))
	else:
		return HttpResponseRedirect(reverse('facemash:choose'))

def board(request,gender):
	u_list = User.objects.filter(user_gender=gender).order_by('-user_rating')
	u_list = u_list[:10]
	context = {'u_list':u_list}
	return render(request,'facemash/board.html',context)














