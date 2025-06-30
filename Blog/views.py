from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from Blog.models import (
    Post, User
)

# Create your views here.


class HomeView(View):
    template_name = 'blog/home.html'
    context = {'title': 'Django Blog App'}

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        query = request.GET.get('search', '')

        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query) |
                Q(author__username__icontains=query)
            )

        self.context['posts'] = posts
        return render(request=request, template_name=self.template_name, context=self.context)


class PostView(View):
    template_name = 'blog/post.html'
    context = {}

    def get(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(slug=kwargs['post_slug'])
        except Post.DoesNotExist:
            messages.error(request, 'No Such Post Exists')
            return redirect('blog_home')

        self.context['post'] = post
        self.context['post_tags'] = post.tags.all()
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
