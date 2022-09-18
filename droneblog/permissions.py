from rest_framework.permissions import BasePermission
from accounts.models.userModel import User


class IsBlogger(BasePermission):

    def permission(self, request):
        try:
            request = request.user.blog_update
        except:
            return False
        return (True if request.user.blog_update.is_verified else False)

    def has_permission(self, request, view):
        return self.permission(request)

    def has_object_permission(self, request, view, obj):
        return self.permission(request)