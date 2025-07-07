from Blog.forms import PostAdminForm
from django.contrib import admin
from Blog.models import (
    Post, Tag
)

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'slug', 'author', 'date_created', 'date_modified']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
