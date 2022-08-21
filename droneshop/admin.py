from django.contrib import admin

from droneshop.models.category import (Category, CategoryByUser)
from droneshop.models.product import (Product, ProductDetailValue, ProductImage, VerificationRequest)
from droneshop.models.orderAcustomer import (orderedItem, customer)

# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryByUser)

# class ProductDetailInline(admin.TabularInline):
#     model = ProductDetail

class ProductImageInline(admin.StackedInline):
    model = ProductImage

class ProductValueInline(admin.TabularInline):
    model = ProductDetailValue

class VerificationRequestInline(admin.StackedInline):
    model = VerificationRequest

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
