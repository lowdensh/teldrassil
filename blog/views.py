from .models import Post
from django.shortcuts import get_object_or_404, render


def blog_posts_all(request):
  list_of_posts = Post.objects.all()
  context = {
    'list_of_posts': list_of_posts,
  }
  return render(request, 'blog/posts_summary.html', context)

def blog_posts_category(request, category):
  list_of_posts = Post.objects.filter(category__name__contains = category)
  context = {
    'list_of_posts': list_of_posts,
    'category': category,
    'filter': True,
    'filter_text': 'Category: ' + category,
  }
  return render(request, 'blog/posts_summary.html', context)

def blog_posts_specific(request, post_id, post_slug):
  post = get_object_or_404(Post, pk=post_id, slug=post_slug)
  context = {
    'post': post,
  }
  return render(request, 'blog/posts_specific.html', context)
