import random

from hashids import Hashids

from django.db import models
from django.urls import reverse
from django.utils import timezone

from authapp.models import BlogUser


class PostCategory(models.Model):
    url = models.URLField(
        verbose_name="category url",
        blank=True,
        unique=True,
    )
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

    def _set_post_category_url(self):
        self.url = f'http://127.0.0.1:8000/post_categories/{self.name}'

    def save(self, *args, **kwargs):
        # TODO: переделать реализацию получения `url`.
        self._set_post_category_url()
        super(PostCategory, self).save()


class Tag(models.Model):
    url = models.URLField(
        verbose_name="tag url",
        blank=True,
        unique=True,
    )
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

    def _set_tag_url(self):
        self.url = f'http://127.0.0.1:8000/tags/{self.name}'

    def save(self, *args, **kwargs):
        # TODO: переделать реализацию получения `url`.
        self._set_tag_url()
        super(Tag, self).save()


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
    url = models.URLField(
        verbose_name="post url",
        null=False,
        unique=True,
        blank=True,
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
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "posts"
        ordering = ("-published_at",)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("mainapp:post-detail", kwargs={'pk': self.pk})

    def _get_salt(self):
        s = sum(map(lambda x: ord(x), self.url))
        salt = chr(random.randint(0, 1000))
        hashids = Hashids(salt=salt)
        return hashids.encode(s)

    def _set_post_url(self):
        self.url = f'http://127.0.0.1:8000/{self.author.id}/' \
                   f'{"-".join(self.title.split())}-{self._get_salt()}'

    def save(self, *args, **kwargs):
        # TODO: переделать реализацию получения `url`.
        self._set_post_url()
        super(Post, self).save()


class Comment(models.Model):
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.RESTRICT,
        verbose_name="post author",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.RESTRICT,
        verbose_name="post",
    )
    parent_id = models.BigIntegerField(
        verbose_name="parent id",
        null=False,
    )
    url = models.URLField(
        verbose_name="post url",
        null=False,
        unique=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="content",
        null=False,
    )
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f"{self.post} - {self.content}"

    def _set_comment_url(self):
        self.url = f'http://127.0.0.1:8000/{self.post.title}/{self.parent_id}/' \
                   f'{self.id}'

    def save(self, *args, **kwargs):
        # TODO: переделать реализацию получения `url`.
        self._set_comment_url()
        super(Comment, self).save()


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.RESTRICT,
    )
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.RESTRICT,
    )