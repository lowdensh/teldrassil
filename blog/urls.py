from . import views
from django.urls import path


appname = 'blog'
urlpatterns = [
    path('', views.posts_all, name='posts_all'),
]
