from django.contrib import admin

from droneservice.models.service import Service, ServiceImage, ServiceVerificationRequest,ServiceDetailValue
from droneservice.models.order import orderedService ,customer
from droneservice.models.category import Category

admin.site.register(Category)
admin.site.register(orderedService)


class ServiceImageInline(admin.StackedInline):
    model = ServiceImage

class ServiceValueInline(admin.TabularInline):
    model = ServiceDetailValue

class VerificationRequestInline(admin.StackedInline):
    model = ServiceVerificationRequest

class OrderInline(admin.StackedInline):
    model = orderedService

@admin.register(customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines= [ServiceImageInline, ServiceValueInline, VerificationRequestInline]
