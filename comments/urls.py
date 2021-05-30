from django.urls import path

from .views import base_view, create_child_comment, create_comment

urlpatterns = [
    path('post-comments/', base_view),
    path('create_comment', create_comment, name='comment_create'),
    path('create_child_comment', create_child_comment, name='comment_child_create'),
]
