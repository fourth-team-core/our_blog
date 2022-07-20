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
    pass


class Post(models.Model):
    pass


class Tag(models.Model):
    url = models.URLField(
        verbose_name='url',
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


class Comment(models.Model):
    pass


class Like(models.Model):
    pass
