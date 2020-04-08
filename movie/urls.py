from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
	path('',views.home,name="home"),
    path('update_to_watch/<movie_id>',views.update_to_watch,name="update_to_watch"),
    path('watch_list',views.watch_list,name="watch_list"),
    path('add_to_seen/<movie_id>',views.add_to_seen,name="add_to_seen"),
    path('seen_list',views.seen_list,name="seen_list"),
    path('search_people',views.search_people,name="search_people"),
    path('all',views.all,name="all"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
