from typing import Iterable
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify
from django.utils.timezone import now


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    def __str__(self) -> str:
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"


class Tag(models.Model):
    caption = models.CharField(max_length=20, null=False, unique=True)
    # posts = models.ManyToManyField()

    def __str__(self) -> str:
        return f"#{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(
        unique=True,
        blank=True,
        # db_index=True -> unique implies db_index and also slugField by default index
    )
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post_data", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.title},{self.author},{self.date}"

    def generate_unique_slug(self):
        original_slug = slugify(self.title)
        if not original_slug:
            original_slug = f"{slugify(self.author)}-1"
        slug = original_slug
        count = 1

        queryset = Post.objects.filter(slug=slug)
        while queryset.exists():
            slug = f"{original_slug}-{count}"
            count += 1
            queryset = Post.objects.filter(slug=slug)
        return slug

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, null=True, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=100)
    user_email = models.EmailField(null=True)
    text = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now=True)

    def save(self):
        if self.name == "Anonymous User":
            self.name = "Anonymous User" + self.pk
        if not self.name:
            self.name = "Anonymous User"
        return super().save()
