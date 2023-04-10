from rest_framework import permissions
from django.contrib.auth import get_user_model



class IsOwnerorRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        path_id = view.kwargs.get('user_id')
        if request.user.id == path_id:
            return True
        
