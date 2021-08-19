from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('view_category', kwargs={'slug': self.slug}) 


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null="", blank=True)
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='category')
    cover_image = models.URLField(null=True, blank=True)
    favorite = models.BooleanField(default=False)
    favorited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.author}'
