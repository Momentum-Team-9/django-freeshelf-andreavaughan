from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ManyToManyField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    book = models.ManyToManyField('Book', related_name='book')

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null="", blank=True)
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='categories')
    cover_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.author}'