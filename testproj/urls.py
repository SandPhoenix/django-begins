from django.conf.urls import patterns, include, url
from django.contrib import admin


# Examples:
# url(r'^$', 'testproj.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls',namespace = 'polls')),
    url(r'^social/',include('social.urls',namespace = 'social')),
    url(r'^hackernews/',include('hackernews.urls',namespace = 'hackernews')),
    url(r'^facemash/',include('facemash.urls',namespace = 'facemash')),
    url(r'^admin/', include(admin.site.urls))
)
