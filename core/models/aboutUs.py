from django.db import models


class Contact(models.Model):
    address = models.TextField()
    phone_number = models.CharField(max_length=13, unique=True, null=False)
    email = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.email


class AboutUs(models.Model):
    context = models.TextField()

    def __str__(self):
        return self.context


class FarmHistory(models.Model):
    year = models.IntegerField(max_length=4)
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True)
    context = models.TextField()

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    image = models.ImageField(upload_to='our_team/')

    def __str__(self):
        return self.image


class Partner(models.Model):
    context = models.TextField()

    def __str__(self):
        return self.context


class PartnerImage(models.Model):
    partner = models.ForeignKey(Partner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return f"Rasm for {self.partner.context[:20]}..."


class Manufacturing(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    context = models.TextField()
    image = models.ImageField(upload_to='manufacturing/')

    def __str__(self):
        return self.title