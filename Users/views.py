from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import RedirectView
from django.views import View
from Users.forms import (
    RegisterForm, LoginForm,
    PostCreateForm, PostEditForm
)
from Blog.models import Post


# Create your views here.


@method_decorator(login_required, name="dispatch")
class MyPostsView(View):
    template_name = 'users/my_posts.html'
    context = {'title': 'My Posts View'}

    def get(self, request, *args, **kwargs):
        self.context['posts'] = Post.objects.filter(author=request.user)
        return render(request=request, template_name=self.template_name, context=self.context)


@method_decorator(login_required, name="dispatch")
class PostCreateView(View):
    template_name = 'users/post_create.html'
    context = {'title': 'Add New Post'}

    def get(self, request, *args, **kwargs):
        self.context['form'] = PostCreateForm()
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('users_my_posts')
        self.context['form'] = form
        return render(request=request, template_name=self.template_name, context=self.context)


@method_decorator(login_required, name="dispatch")
class PostDeleteView(View):
    template_name = 'users/post_delete.html'
    context = {'title': 'Delete Post'}

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['post_pk'], author=request.user)
        self.context['post'] = post
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['post_pk'], author=request.user)
        post.delete()
        return redirect('users_my_posts')


@method_decorator(login_required, name="dispatch")
class PostEditView(View):
    template_name = 'users/post_edit.html'
    context = {'title': 'Edit Post'}

    def get(self, request, *args, **kwargs):

        post = Post.objects.get(pk=kwargs['post_pk'], author=request.user)

        self.context['form'] = PostEditForm(instance=post)
        self.context['post'] = post

        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):

        post = Post.objects.get(pk=kwargs['post_pk'], author=request.user)

        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('users_post_edit', kwargs['post_pk'])

        self.context['form'] = form
        self.context['post'] = post

        return render(request=request, template_name=self.template_name, context=self.context)


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('blog_home')


class LoginView(View):
    template_name = 'users/login.html'
    context = {'title': 'Login View'}

    def get(self, request, *args, **kwargs):
        self.context['form'] = LoginForm()
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog_home')

        self.context['form'] = form
        return render(request=request, template_name=self.template_name, context=self.context)


class RegisterView(View):
    template_name = 'users/register.html'
    context = {'title': 'Register View'}

    def get(self, request, *args, **kwargs):
        self.context['form'] = RegisterForm()
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
        self.context['form'] = form
        return render(request=request, template_name=self.template_name, context=self.context)
