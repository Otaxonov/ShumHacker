from Blog.models import Post
from django import template

register = template.Library()

@register.simple_tag()
def get_posts():
    return Post.objects.all()


@register.inclusion_tag('blog/list_posts.html')
def show_posts():
    posts = Post.objects.all()
    return {'custom_posts': posts}
