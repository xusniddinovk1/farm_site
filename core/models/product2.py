from django.db import models
from django.urls import reverse
from .misc import Category, Animal


class Equipment(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='equipments/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('equipment_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'


class Paint(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='paints/')
    dosage = models.TextField()
    animals = models.ManyToManyField(Animal, related_name='paints')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('paint_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Paint'
        verbose_name_plural = 'Paints'


class Work(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    context = models.TextField()
    image = models.ImageField(upload_to='equipments/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
