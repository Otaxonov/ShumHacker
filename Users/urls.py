from django.urls import path
from Users.views import (
    RegisterView, LoginView, LogoutView,
    MyPostsView, PostCreateView, PostEditView,
    PostDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='users_register'),
    path('login/', LoginView.as_view(), name='users_login'),
    path('logout/', LogoutView.as_view(), name='users_logout'),
    path('my-posts/', MyPostsView.as_view(), name='users_my_posts'),
    path('my-posts/create-post/', PostCreateView.as_view(), name='users_post_create'),
    path('my-posts/edit-post/<int:post_pk>/', PostEditView.as_view(), name='users_post_edit'),
    path('my-posts/delete-post/<int:post_pk>/', PostDeleteView.as_view(), name='users_post_delete'),
]
