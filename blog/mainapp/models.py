from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    pass


class BlogUser(AbstractUser):
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to='',
        blank=True,
    )
    age = models.PositiveIntegerField(
        verbose_name='age',
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = 'blog_users'
        verbose_name = 'blog user'
        verbose_name_plural = 'blog users'

    def __str__(self):
        return f'{self.username} {self.is_staff} {self.is_superuser} ' \
               f'{self.is_deleted}'


class BlogUserProfile(models.Model):
    user = models.OneToOneField(
        BlogUser,
        on_delete=models.RESTRICT,
        unique=True,
    )
    # TODO: нужен ли отдельный класс или достаточно расширение абстрактного?


class PostCategory(models.Model):
    url = models.URLField(
        verbose_name='category url',
    )
    name = models.CharField(
        max_length=64,
        verbose_name='category name',
        unique=True,
    )

    class Meta:
        db_table = 'post_categories'
        verbose_name = 'post category'
        verbose_name_plural = 'post categories'

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    url = models.URLField(
        verbose_name='tag url',
    )
    name = models.CharField(
        verbose_name='tag name',
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = 'tags'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.RESTRICT,
        verbose_name='post author',
    )
    # TODO: принять решение - в нашем случае может ли пост относится к разным
    #  категориям одновременно? Если да, то нужно many-to-many field
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.RESTRICT,
        verbose_name='post category',
    )
    title = models.CharField(
        max_length=128,
        verbose_name='post title',
        null=False,
    )
    url = models.URLField(
        verbose_name='post url',
        null=False,
        unique=True,
    )
    content = models.TextField(
        verbose_name='content',
        null=False,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='post_tags',
    )
    published = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.RESTRICT,
        verbose_name='post author',
    )
    # TODO: принять решение - в нашем случае может ли пост относится к разным
    #  категориям одновременно? Если да, то нужно many-to-many field
    post = models.ForeignKey(
        Post,
        on_delete=models.RESTRICT,
        verbose_name='post',
    )
    parent_id = models.BigIntegerField(
        verbose_name='parent id',
        null=False,
    )
    url = models.URLField(
        verbose_name='post url',
        null=False,
        unique=True,
    )
    content = models.TextField(
        verbose_name='content',
        null=False,
    )
    published = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    pass
