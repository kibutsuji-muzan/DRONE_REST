from django.contrib import admin
from droneservice.models.service import Service, ServiceDetail, ServiceDetailValue, ServiceType

# Register your models here.
admin.site.register(Service) 
admin.site.register(ServiceType)

class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail

class ServiceValueInline(admin.TabularInline):
    model = ServiceDetailValue

class ServiceTypeAdmin(admin.ModelAdmin):
    inlines = [ServiceDetailInline]

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceValueInline]
