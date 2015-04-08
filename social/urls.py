from django.conf.urls import patterns, url
from social import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^post/$',views.post,name='post'),
	url(r'^signup/$',views.signup,name='signup')
)