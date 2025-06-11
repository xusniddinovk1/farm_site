from django.db import models
from .misc import Category, Animal
from django.urls import reverse


class CleaningProducts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=200, null=True, blank=True)
    animal = models.ManyToManyField(Animal, related_name='cleaning_products')
    manufacturer = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/')
    about = models.TextField()
    structure = models.TextField()
    usage = models.TextField()
    packaging = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cleaningproduct_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Cleaning Product'
        verbose_name_plural = 'Cleaning Products'


class VitaminsMinerals(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=200, null=True, blank=True)
    animal = models.ManyToManyField(Animal, related_name='vitamins_minerals')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='vitamins/')
    effect = models.TextField()
    dosage = models.TextField()
    contraindications = models.TextField()
    instruction = models.TextField()
    packaging = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vitamin_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Vitamin/Mineral'
        verbose_name_plural = 'Vitamins/Minerals'
