from Blog.forms import PostAdminForm
from django.contrib import admin
from Blog.models import (
    Post, Tag, User
)

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'slug', 'author', 'date_created', 'date_modified', 'extra_info']
    list_editable = ('slug', 'author')
    search_fields = ['title', 'author__username']
    list_per_page = 5
    prepopulated_fields = {'slug': ('title',)}
    actions = ['set_default_author']
    # ordering = ['']
    # exclude = ['author']
    # fields = ['title', 'slug']
    readonly_fields = ['author']

    @admin.display(description='title chars count')
    def extra_info(self, post: Post):
        return f'chars: {len(post.title)}'

    @admin.action(description='set default author')
    def set_default_author(self, request, queryset):
        user = User.objects.get(pk=1)
        queryset.update(author=user)
        self.message_user(request, 'Posts updated for default author')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
