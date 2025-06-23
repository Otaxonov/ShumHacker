from django.urls import path
from Blog.views import (
    HomeView, PostView,
    UserPostsView, UserPostView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('posts/<int:post_pk>/', PostView.as_view(), name='blog_post'),
    path('user/<int:user_pk>/posts/', UserPostsView.as_view(), name='blog_user_posts'),
    path('user/<int:user_pk>/posts/<int:post_pk>/', UserPostView.as_view(), name='blog_user_post'),
]
