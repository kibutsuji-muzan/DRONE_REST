from django.contrib import admin

from accounts.models.portfolio import Portfolio, PortfolioPost, PostImage
from extras.models.contactUs import ContactUs, Complaints, Reports, Review

class PostImageInline(admin.TabularInline):
    model = PostImage

class PostInline(admin.TabularInline):
    model = PortfolioPost

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PostInline]

@admin.register(PortfolioPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

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

