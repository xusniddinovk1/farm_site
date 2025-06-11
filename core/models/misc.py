from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Animal(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'


class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    context = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Gallery(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"Gallery Image ({self.id})"

    class Meta:
        ordering = ['id']
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
