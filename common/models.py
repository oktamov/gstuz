from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Document(models.Model):
    class DocumentTypes(models.TextChoices):
        DOCUMENT = "document"
        CERTIFICATE = "certificate"
        PROJECT = "project"

    title = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='files/')
    type = models.CharField(max_length=30, choices=DocumentTypes.choices)

    def __str__(self):
        return self.title


class Form(models.Model):
    full_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    desc = models.TextField()

    def __str__(self):
        return self.full_name


class Region(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=55)
    region = models.ForeignKey('common.Region', on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name


class Address(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    metro = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey('common.District', on_delete=models.SET_NULL, null=True, related_name='address')

    def __str__(self):
        return self.address1


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    web_site = models.CharField(max_length=255, null=True, blank=True)
    address = models.ManyToManyField('common.Address', blank=True, related_name='companies')

    def __str__(self):
        return self.name

