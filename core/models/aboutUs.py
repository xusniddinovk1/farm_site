from django.db import models
from django.urls import reverse


class Contact(models.Model):
    address = models.TextField()
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class AboutUs(models.Model):
    context = models.TextField()

    def __str__(self):
        return self.context[:50]  # kontekstdan 50 belgini ko‘rsatamiz

    class Meta:
        ordering = ['id']
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class FarmHistory(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    context = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.title}"

    def get_absolute_url(self):
        return reverse('farmhistory_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-year']
        verbose_name = 'Farm History'
        verbose_name_plural = 'Farm Histories'


class OurTeam(models.Model):
    image = models.ImageField(upload_to='our_team/')

    def __str__(self):
        return f"OurTeam Image ({self.id})"

    class Meta:
        ordering = ['id']
        verbose_name = 'Our Team'
        verbose_name_plural = 'Our Team'


class Partner(models.Model):
    context = models.TextField()

    def __str__(self):
        return self.context[:50]

    class Meta:
        ordering = ['id']
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


class PartnerImage(models.Model):
    partner = models.ForeignKey(Partner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return f"Image for {self.partner.context[:20]}..."

    class Meta:
        ordering = ['id']
        verbose_name = 'Partner Image'
        verbose_name_plural = 'Partner Images'


class Manufacturing(models.Model):
    title = models.CharField(max_length=200)
    context = models.TextField()
    image = models.ImageField(upload_to='manufacturing/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Manufacturing'
        verbose_name_plural = 'Manufacturing'
