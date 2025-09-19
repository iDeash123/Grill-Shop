from .models import Category, Product
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'slug',
        'price', 'discount', 'stock', 'available',
        'created', 'updated'
    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'discount', 'stock', 'available']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
