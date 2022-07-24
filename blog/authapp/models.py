from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    """
    Main model for user within the project
    """
    is_author = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
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
        return self.get_full_name()


class BlogUserProfile(models.Model):
    """
    Main model for user profile within the project
    """
    user = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE,
        unique=True,
    )
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to='',
        blank=True,
    )
    age = models.PositiveIntegerField(
        verbose_name='age',
    )
    about = models.TextField(
        verbose_name='about me',
        blank=True,
    )

    class Meta:
        db_table = 'blog_user_profiles'
        verbose_name = 'blog user profile'
        verbose_name_plural = 'blog user profiles'

    def __str__(self):
        return self.user
