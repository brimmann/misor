from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

admin.site.register(Product, ProductAdmin)
