from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from app.models import *

# Create your views here.

def index(request):
	#return HttpResponse("Hello, world. Your're at the poll index.")
	artists = Artist.objects.all() 
	return render_to_response('artist.html', {'artists' : artists}) #looks in templates folder by default configuration

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def artistdetails(request, id):
	artist = Artist.objects.get(pk = id)
	return render_to_response('artistdetails.html', {'artist' : artist})

def artist_albums(request, id):
	artist = Artist.objects.get(pk = id)
	albums = Album.objects.filter(artist__exact = artist)
	return render_to_response('artist_albums.html',{'albums' : albums})
	#return HttpResponse(id)

def create(request):
	if request.method == "GET" :
		form = ArtistForm()
		#return HttpResponse("Add an artist?")
		return render(request, 'addartist.html',{'form' : form})
	elif request.method == "POST" :
		form = ArtistForm(request.POST)
		form.save()
		return HttpResponseRedirect('/artist')
	
