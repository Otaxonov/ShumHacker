from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
