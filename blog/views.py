from .models import Post
from django.shortcuts import render


def posts_all(request):
    list_of_posts = Post.objects.all()
    context = {
        'list_of_posts': list_of_posts,
    }
    return render(request, 'blog/posts_all.html', context)
