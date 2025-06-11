from django.db import models
from .misc import Category, Animal


class VeterinaryDrugs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=150, null=True, blank=True)
    animals = models.ManyToManyField(Animal, related_name='products')
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique=True)
    structure = models.CharField(max_length=150, null=True, blank=True)
    instruction = models.TextField()
    dosage = models.TextField()
    release_period = models.CharField(max_length=10, null=True, blank=True)
    manufacturer = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.title


class Vaccine(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    for_what = models.CharField(max_length=150, null=True, blank=True)
    structure = models.TextField()
    animals = models.ManyToManyField(Animal, related_name='products')
    manufacturer = models.CharField(max_length=150, null=True, blank=True)
    drug = models.TextField()
    usage = models.TextField()
    expiration_date = models.TextField()
    storage = models.TextField()

    def __str__(self):
        return self.title
