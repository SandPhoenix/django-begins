from django.conf.urls import patterns, url
from facemash import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>\d+)/$',views.detail,name='detail'),
    # url(r'^(?P<question_id>\d+)/results/$',views.results,name='results'),
    url(r'^vote/(?P<lose_id>\d+)/(?P<win_id>\d+)/$',views.vote,name='vote'),
    url(r'^(?P<gender>[mf])/choose/$',views.choose,name='choose'),
    url(r'^(?P<gender>[mf])/rankings/$',views.board,name='board'),

)