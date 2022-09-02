from django.contrib import admin

from droneblog.models.blogs import BlogImage, Blog, BlogComplaints


# Register your models here.

class BlogImageInline(admin.StackedInline):
    model = BlogImage

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]

@admin.register(BlogComplaints)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('blog',)