
from django.conf.urls import url
#import views
from app import views

urlpatterns = [
    #url(r'^polls/', include('polls.urls')),
    url(r'^$', views.index, name='index'),
	url(r'^(?P<id>\d+)/$', views.artistdetails, name='details'),
    url(r'^(?P<id>\d+)/albums/$', views.artist_albums, name="albumlist"),
	url(r'^create/$', views.create, name="addartist"),
    #url(r'^(?P<question_id>[0-9]+)/$', views.results, name='results'),
]
