from django.db import models

from .misc import Category, Animal


class CleaningProducts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=200, null=True, blank=True)
    animal = models.ManyToManyField(Animal, related_name='products')
    manufacturer = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(unique=True)
    about = models.TextField()
    structure = models.TextField()
    usage = models.TextField()
    packaging = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class VitaminsMinerals(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=200, null=True, blank=True)
    animal = models.ManyToManyField(Animal, related_name='products')
    title = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(unique=True)
    effect = models.TextField()
    dosage = models.TextField()
    contraindications = models.TextField()
    instruction = models.TextField()
    packaging = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
