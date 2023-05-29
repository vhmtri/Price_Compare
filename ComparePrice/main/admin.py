from django.contrib import admin
from .models import Category, Brand, Store, Product, Price

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Đúng rồi
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Đúng rồi
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', )  # Đúng rồi
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'image_url', 'description')  # Thêm 'image_url' và 'description'
    list_filter = ('category', 'brand',)
    search_fields = ('name', 'category__name', 'brand__name',)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'price', 'date', 'product_url')
    list_filter = ('store', 'date',)
    search_fields = ('product__name', 'store__name',)