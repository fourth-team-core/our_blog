from django.db import models
from django.urls import reverse

from authapp.models import BlogUser


class PostCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="category name",
        unique=True,
    )

    class Meta:
        db_table = "post_categories"
        verbose_name = "post category"
        verbose_name_plural = "post categories"

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name="tag name",
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "tags"
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    STATUS_CHOICES = {
        ("draft", "Draft"),
        ("published", "Published"),
    }
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.RESTRICT,
        verbose_name="post author",
    )
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.RESTRICT,
        verbose_name="post category",
    )
    title = models.CharField(
        max_length=128,
        verbose_name="post title",
        null=False,
    )
    content = models.TextField(
        verbose_name="content",
        null=False,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="post_tags",
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
    )
    likes_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "posts"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("mainapp:post-detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    """ Comment """
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        verbose_name="post author",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="post",
    )
    content = models.TextField(
        verbose_name="content",
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True,
                                 help_text="If True, the comment will be shown on page"
                                )

    class Meta:
        db_table = "comments"
        ordering = ('-created_at',)

    def __str__(self):
        return f"Comment by  {self.author} on {self.post}"


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.RESTRICT,
    )
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.RESTRICT,
    )
