from django.shortcuts import render,redirect
from django.contrib import messages

import requests
import os

from .models import Movie

API_KEY = os.getenv('TMDB_API_KEY')


#SEARCH API
def home(request):
	"""    SEARCH BY MOVIE NAME    """

	searchMovieField = request.GET.get('search_movie')


	url = f"https://api.themoviedb.org/3/search/movie?query={searchMovieField}&api_key={API_KEY}"
	movie_list = []
	if request.method == "GET":
		if searchMovieField != "":
			r = requests.get(url).json()

			
			try:
				for  i in range(len(r['results'])):
					movie_info = {"title": r['results'][i]['title'],
								 'overview':r['results'][i]['overview'],
								 'poster_path':r['results'][i]['poster_path'],
								 'release_date':r['results'][i]['release_date'],
								 'vote_average':r['results'][i]['vote_average'],
								 'id':r['results'][i]['id']
								 }

			
					movie_list.append(movie_info)
			except KeyError:
				pass
			except Exception as e:
				pass

	context = {'movie_list':movie_list}

	return render(request,'movie/home.html',context)



def search_people(request):
	"""  SEARCH BY PERSON NAME """

	searchPeopleField = request.GET.get('search_people')
	url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={searchPeopleField}"
	people_list = []
	if request.method == "GET":
		if searchPeopleField != "":
			r = requests.get(url).json()
			

			for  i in range(len(r['results'])):
				peopleInfo ={
							'profile_path':r['results'][i]['profile_path'],
							'known_for_department':r['results'][i]['known_for_department'],
							'gender':r['results'][i]['gender'],
							'id':r['results'][i]['id'],
							'movies':r['results'][i]['known_for'],
							'name':r['results'][i]['name']
							}
				
				
				people_list.append(peopleInfo)
				
	context = {'people_list':people_list}			
	return render(request,'movie/search_people.html',context)




def update_to_watch(request,movie_id):
	"""    ADD TO WATCH LIST AND DELETE TO WATCH LIST     """


	movie = Movie.objects.filter(movie_id=movie_id)
	if movie.exists():
		movie.delete()
		messages.info(request,'This movie removed from WatchList.')
	else:
		Movie.objects.create(movie_id=movie_id)

	return redirect('watch_list')


#VIEW WATCH_LIST
def watch_list(request):
	movies = Movie.objects.all()
	url = "https://api.themoviedb.org/3/movie/{}?api_key={}"
	watch_list = []
	for movie in movies:
		r = requests.get(url.format(movie.movie_id,API_KEY),stream=True).json()
		movie_info = {
					"title":r['title'],
					"poster_path":r['poster_path'],
					"vote_average":r['vote_average'],
					"id":r['id'],
					"is_seen":movie.is_seen
		}
		watch_list.append(movie_info)
	context = {'watch_list':watch_list}
	return render(request,'movie/watch_list.html',context)



def add_to_seen(request,movie_id):
	"""    İF YOU WATCHED TO MOVİE THEN CHANGE TO MOVIE is_seen TO TRUE       """

	movie = Movie.objects.get(movie_id=movie_id)
	movie.is_seen = True
	movie.save()
	return redirect('watch_list')


#VIEW SEEN LIST
def seen_list(request):
	"""       LIST OF  WATCHED MOVIE         """

	movies = Movie.objects.all()
	url = "https://api.themoviedb.org/3/movie/{}?api_key={}"
	seen_list = []
	for movie in movies:
		if movie.is_seen:
			r = requests.get(url.format(movie.movie_id,API_KEY)).json()
			movie_info = {
						"title":r['title'],
						"poster_path":r['poster_path'],
						"vote_average":r['vote_average'],
						"id":r['id'],
						"is_seen":movie.is_seen,
			}
			seen_list.append(movie_info)
	context = {'seen_list':seen_list}
	return render(request,'movie/seen_list.html',context)






