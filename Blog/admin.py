from django.contrib import admin
from Blog.models import (
    Post
)

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created', 'date_modified']
