from django.contrib import admin

from .models import Post
from .models import PostCategory
from .models import Tag
from .models import Comment
from .models import Like


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', )


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def display_author_name(self, obj: Post) -> str:
        return obj.author.username

    def display_post_category(self, obj: Post) -> str:
        return obj.category.name

    display_author_name.short_description = 'Author'
    display_post_category.short_description = 'Post category'
    list_display = (
        'id',
        'display_author_name',
        'display_post_category',
        'title',
        'status',
    )
    search_fields = (
        'id',
        'author__username',
        'category__name',
        'title',
        'status',
    )
    list_filter = ('author__username', 'category__name', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    def display_author_name(self, obj: Comment) -> str:
        return obj.author.username

    def display_post_title(self, obj: Comment) -> str:
        return obj.post.title

    display_author_name.short_description = 'Author'
    display_post_title.short_description = 'Post title'
    list_display = (
        'display_author_name',
        'display_post_title',
    )
    search_fields = ('author__username', 'post__title',)
    list_filter = ('author__username', 'post__title',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    def display_author_name(self, obj: Like) -> str:
        return obj.author.username

    def display_post_title(self, obj: Like) -> str:
        return obj.post.title

    display_author_name.short_description = 'Author'
    display_post_title.short_description = 'Post title'

    list_display = (
        'display_author_name',
        'display_post_title',
    )
    search_fields = ('author__username', 'post__title')
    list_filter = ('author__username', 'post__title')
