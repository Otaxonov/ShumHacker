from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    content = models.TextField()
    poster = models.ImageField(upload_to='blog/post/uploads', default='blog/post/default.png', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
