from . import views
from django.urls import path


appname = 'blog'
urlpatterns = [
  path(
    '',
    views.blog_posts_all,
    name='blog_posts_all'
  ),
  path(
    'category/<category>/',
    views.blog_posts_category,
    name='blog_posts_category'
  ),
  path(
    'tag/<tag>/',
    views.blog_posts_tag,
    name='blog_posts_tag'
  ),
  path(
    'post/<int:post_id>/<slug:post_slug>/',
    views.blog_posts_specific,
    name='blog_posts_specific'
  ),
]
