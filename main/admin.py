from django.contrib import admin

from main.models import Category, Product


class CategoriesInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1
    min_num = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInline,
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    inlines = [
        CategoriesInline,
    ]
    exclude = ('categories',)
