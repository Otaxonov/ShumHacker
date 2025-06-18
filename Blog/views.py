from django.shortcuts import render
from django.views import View
from Blog.models import (
    Post, User
)

# Create your views here.


class HomeView(View):
    template_name = 'blog/home.html'
    context = {'title': 'Django Blog App'}

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name, context=self.context)


class PostsView(View):
    template_name = 'blog/posts.html'
    context = {'title': 'Posts View'}

    def get(self, request, *args, **kwargs):
        self.context['posts'] = Post.objects.all()
        return render(request=request, template_name=self.template_name, context=self.context)


class PostView(View):
    template_name = 'blog/post.html'
    context = {}

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['post_pk'])

        self.context['post'] = post
        self.context['title'] = post.title
        return render(request=request, template_name=self.template_name, context=self.context)


class UserPostsView(View):
    template_name = 'blog/user_posts.html'
    context = {}

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_pk'])
        posts = Post.objects.filter(author=user)

        self.context['posts'] = posts
        self.context['title'] = f'{user.username} Posts'
        return render(request=request, template_name=self.template_name, context=self.context)


class UserPostView(View):
    template_name = 'blog/user_post.html'
    context = {}

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_pk'])
        post = Post.objects.get(pk=kwargs['post_pk'], author=user)

        self.context['post'] = post
        self.context['title'] = post.title
        return render(request=request, template_name=self.template_name, context=self.context)
