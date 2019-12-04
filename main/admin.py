from django.contrib import admin

from main.models import Product, Company, Category


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ['name', 'logo']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'school_type', 'expiration_date']
    search_fields = ['name', 'description']
    list_filter = ['expiration_date', 'categories', 'company']

    def groupe(self, obj):
        participant = Category.objects.filter(product=obj.username)
        if participant.group:
            return participant.group.name
        return '-'
