from django.db import models
from django.urls import reverse

from .misc import Category, Animal


class Aminoacid(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=200, null=True, blank=True)
    animal = models.ManyToManyField(Animal, related_name='aminoacids')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='aminoacids/')
    manufacturer = models.CharField(max_length=150)
    effect = models.TextField()
    instruction = models.TextField()
    advantages = models.TextField()
    preparation = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('aminoacid_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Amino Acid'
        verbose_name_plural = 'Amino Acids'


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=200, null=True, blank=True)
    animal = models.ManyToManyField(Animal, related_name='foods')
    manufacturer = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='foods/')
    effect = models.TextField()
    instruction = models.TextField()
    packaging = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
