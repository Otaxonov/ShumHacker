from django.shortcuts import redirect
from django.contrib import messages
from Blog.models import Post
from functools import wraps


def check_post(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            post = Post.objects.get(slug=kwargs['post_slug'])
        except Post.DoesNotExist:
            messages.error(request, 'No Such Post Exists')
            return redirect('blog_home')
        kwargs['post'] = post
        return view_func(request, *args, **kwargs)
    return wrapper
