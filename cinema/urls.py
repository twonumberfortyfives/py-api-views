from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView,
    CinemaHallSet,
)

cinema_hall_list = CinemaHallSet.as_view(
    actions={
        'get': 'list',
        'post': 'create',
    }
)

cinema_hall_detail = CinemaHallSet.as_view(
    actions={
        'get': "retrieve",
        'put': "update",
        'patch': "partial_update",
        'delete': "destroy",
    }
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>", ActorDetailView.as_view(), name="actor-detail"),
    path("cinemahalls/", cinema_hall_list, name="cinema-hall-list"),
    path("cinemahalls/<int:pk>", cinema_hall_detail, name="cinema-hall-detail")
]

app_name = "cinema"
