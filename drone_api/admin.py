from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from drone_api.models.category import Category, CategoryByUser
from drone_api.models.product import *
from drone_api.models.service import *

# Register your models here.
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(CategoryByUser)
#Products

class ProductDetailsInline(admin.TabularInline):
    model = ProductDetail

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductDetailsInline]

class ProductImageInline(admin.StackedInline):
    model = ProductImage

class ProductDetailValueInline(admin.TabularInline):
    model = ProductDetailValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductDetailValueInline]

#Services

# class ServiceDetailsInline(admin.TabularInline):
#     model = ServiceDetail

# @admin.register(ServiceType)
# class ServiceTypeAdmin(admin.ModelAdmin):
#     inlines = [ServiceDetailsInline]

# class ServiceDetailValueInline(admin.TabularInline):
#     model = ServiceDetailValue

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     inlines = [ServiceDetailValueInline]
