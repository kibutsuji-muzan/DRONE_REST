from django.contrib import admin

from droneshop.models.category import (Category, CategoryByUser)
from droneshop.models.product import (Product, ProductDetailValue, ProductImage, ProductVerificationRequest)
from droneshop.models.orders import (orderedItem, customer)

# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryByUser)
admin.site.register(ProductVerificationRequest)

class ProductImageInline(admin.StackedInline):
    model = ProductImage

class ProductValueInline(admin.TabularInline):
    model = ProductDetailValue

class VerificationRequestInline(admin.StackedInline):
    model = ProductVerificationRequest

class OrderInline(admin.StackedInline):
    model = orderedItem

@admin.register(customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

# @admin.register(ProductType)
# class ProductTypeAdmin(admin.ModelAdmin):
#     inlines = [ProductDetailInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines= [ProductImageInline, ProductValueInline, VerificationRequestInline]
