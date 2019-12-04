from django.contrib import admin

from main.models import Category, Product


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    inlines = [CategoryInline]
