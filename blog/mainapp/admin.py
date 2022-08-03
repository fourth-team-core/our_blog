from django.contrib import admin

from .models import Post
from .models import PostCategory
from .models import Tag
from .models import Comment
from .models import Like

from authapp.models import BlogUser
from authapp.models import BlogUserProfile


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'url')


class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ('url', 'name')
    list_display = ('id', 'url', 'name')


class PostAdmin(admin.ModelAdmin):
    def display_author_name(self, obj: Post) -> str:
        return obj.author.username

    def display_post_category(self, obj: Post) -> str:
        return obj.category.name

    # def display_tags(self, obj: Post) -> str:
    #     return obj.tags

    display_author_name.short_description = 'Author'
    display_post_category.short_description = 'Post category'
    # display_tags.short_description = 'Tags'

    list_display = (
        'id',
        'display_author_name',
        'display_post_category',
        'title',
        # 'display_tags',
        'status',
    )


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
