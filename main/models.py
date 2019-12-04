from django.core.validators import MinValueValidator
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from main.constants import SCHOOL_TYPES


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = ThumbnailerImageField(upload_to='companies_logos/', blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return "{}".format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='products_photos/')
    categories = models.ManyToManyField(Category, related_name='categories')
    school_type = models.PositiveSmallIntegerField(choices=SCHOOL_TYPES, default=1, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)], )
    expiration_date = models.DateField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return "{}".format(self.name)