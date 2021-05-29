from django.shortcuts import render

from .models import Post
from .utils import create_comments_tree


def base_view(requests):
    comments = Post.objects.first().comments.all()
    result = create_comments_tree(comments)
    return render(requests, 'base.html', {'comments': result})
