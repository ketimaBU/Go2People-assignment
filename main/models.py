from django.db import models

from main.constants import SCHOOL_TYPES


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='companies_logos/')

    def __str__(self):
        return "{}".format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='products_photos/')
    categories = models.ManyToManyField(Category, related_name='categories')
    schooltype = models.PositiveSmallIntegerField(choices=SCHOOL_TYPES, default=1, blank=True)
    price = models.FloatField()
    expiration_date = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return "{}".format(self.name)
