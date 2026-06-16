from django.contrib import admin
from .models import Product, Category

# Register your models here.

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']
    list_filter = ['category']


admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name']
    search_fields = ['name', 'slug']
