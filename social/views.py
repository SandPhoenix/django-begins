from django.shortcuts import render,get_object_or_404,render_to_response
from social.models import User,Post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def check_user(request):
	try:
		username = request.POST['user']
		try:
			username = User.objects.get(username=username)
		except User.DoesNotExist:
			username = ''
	except KeyError:
		try:
			username = request.session['user_id']
			try:
				username = User.objects.get(id=username)
			except User.DoesNotExist:
				username = ''
		except KeyError:
			username = ''
	return username

def index(request):
	post_list = Post.objects.order_by('-post_date')
	u = check_user(request)
	should_log_in = bool(request.POST.get('should_log_in',True))
	if should_log_in == False:
		request.session.flush()
		request.session['logged_in'] = False
		logged_in = False
	else:
		logged_in = request.session.get('logged_in',False)
		if u != '' and logged_in == False:
			try:
				if u.password == request.POST['pass']:
					request.session.set_expiry(7200)
					request.session['user_id'] = u.id
					request.session['logged_in'] = True
					u = u.username
				else:
					u = ''
			except KeyError:
				u = ''
		logged_in = request.session.get('logged_in',False)
	return render(request,'social/index.html',{'post_list':post_list,'username':u,'logged_in':logged_in})

def post(request):
	u = check_user(request)
	post = ''
	try:
		post = request.POST['post_text']
	except KeyError:
		post = ''
	if u != '' and post != '':
		u.action_post(post)
	return HttpResponseRedirect(reverse('social:index'))

def signup(request):
	should_sign_up = bool(request.POST.get('should_sign_up',''))
	if should_sign_up == True:
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		first_name = request.POST.get('first_name','')
		last_name = request.POST.get('last_name','')
		old_users = [i.username for i in User.objects.all()]
		if username != '' and password != '' and first_name != '' and last_name != '' and len(password) >= 8 and username not in old_users:
			u = User(username=username,password=password,first_name=first_name,last_name=last_name)
			u.save()
			return HttpResponseRedirect(reverse('social:index'))
		else:
			return render(request,'social/sign_up.html',{})
	else:
		return render(request,'social/sign_up.html',{})



	