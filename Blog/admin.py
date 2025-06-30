from django.contrib import admin
from Blog.models import (
    Post
)

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'date_created', 'date_modified']
    prepopulated_fields = {'slug': ('title',)}
