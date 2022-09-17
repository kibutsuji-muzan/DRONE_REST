from rest_framework.permissions import BasePermission
from accounts.models.userModel import User


def IsSameUser(user, pk):
    try:
        return (True if (User.objects.get(id=pk)==user) else False)
    except:
        return False


class IsWorker(BasePermission):

    def permission(self, request):
        try:
            request = request.user.update_request
        except:
            return False
        return (True if request.user.update_request.is_verified else False)

    def has_permission(self, request, view):
        return self.permission(request)
        
    def has_object_permission(self, request, view, obj):
        return self.permission(request)