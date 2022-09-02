from django.contrib import admin

from extras.models.portfolio import Portfolio, PortfolioDetailValue, PortfolioImage
from extras.models.contactUs import ContactUs, Complaints, Reports, Review

class PortfolioDetailInline(admin.TabularInline):
    model = PortfolioDetailValue

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline, PortfolioDetailInline]

@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('service','title')

@admin.register(ContactUs)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('phone','email')

@admin.register(Reports)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('product','title')

@admin.register(Review)
class ComplaintsAdmin(admin.ModelAdmin):
    pass