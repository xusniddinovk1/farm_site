from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Animal(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True)
    context = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='photos/')