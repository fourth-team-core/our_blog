from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


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
        return self.username


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
        null=True, 
        blank=True,
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
        return self.user.username


    def create_profile(sender, instance, created, **kwargs):
        try:
            instance.bloguserprofile.save()
        except ObjectDoesNotExist:
            BlogUserProfile.objects.create(user=instance)

    def save_profile(sender, instance, **kwargs):
        instance.bloguserprofile.save()

    post_save.connect(create_profile, sender=BlogUser)
    post_save.connect(save_profile, sender=BlogUser)