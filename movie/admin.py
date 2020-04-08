from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
	list_display = ('movie_id','is_seen') 
	class Meta:
		model = Movie




admin.site.register(Movie,MovieAdmin)
