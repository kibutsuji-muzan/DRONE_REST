from django.contrib import admin
from droneservice.models.service import Service, ServiceImage, ServiceVerificationRequest,ServiceDetailValue
from droneservice.models.order import orderedService ,customer
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

# @admin.register(ServiceType)
# class ServiceTypeAdmin(admin.ModelAdmin):
#     inlines = [ServiceDetailInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines= [ServiceImageInline, ServiceValueInline, VerificationRequestInline]
