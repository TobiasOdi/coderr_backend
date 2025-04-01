from rest_framework import permissions
from profile_app.models import Profile
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user or request.user.is_staff
    
class ListCreateOfferPermission(permissions.BasePermission):
    """
    Custom permission to allow:
    - Anyone to read (GET)
    - Authenticated users to create (POST)
    - Owners to update (PATCH)
    - Admins to delete (DELETE)
    """

    def has_permission(self, request, view):
        if request.method in ["POST", "PATCH", "DELETE"]:
            return request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            current_profile = Profile.objects.filter(user=request.user)
            return obj.type == current_profile["type"]
             # return obj.auth_user == request.user or request.user.is_staff
        return False
    
class IsOwnerOfferPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PATCH", "DELETE"]:
            return obj.user == request.user or request.user.is_staff
        return False

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(LimitOffsetPagination):
    page_size = 1
    page_size_query_param = 'page_size'
