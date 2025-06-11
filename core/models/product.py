from django.db import models
from django.urls import reverse

from .misc import Category, Animal


class VeterinaryDrugs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    for_what = models.CharField(max_length=150, null=True, blank=True)
    animals = models.ManyToManyField(Animal, related_name='veterinary_drugs')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    structure = models.CharField(max_length=150, null=True, blank=True)
    instruction = models.TextField()
    dosage = models.TextField()
    release_period = models.CharField(max_length=10, null=True, blank=True)
    manufacturer = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('drug_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Vaccine(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    for_what = models.CharField(max_length=150, null=True, blank=True)
    structure = models.TextField()
    animals = models.ManyToManyField(Animal, related_name='vaccines')
    manufacturer = models.CharField(max_length=150, null=True, blank=True)
    drug = models.TextField()
    usage = models.TextField()
    expiration_date = models.TextField()
    storage = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vaccine_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
