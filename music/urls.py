from . import views
from django.urls import path


appname = 'music'
urlpatterns = [
  path(
    '',
    views.music_tracks_all,
    name='music_tracks_all'
  ),
]
