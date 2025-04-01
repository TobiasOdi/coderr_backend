from rest_framework import permissions

# class IsOwnerOrAdmin(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.user == request.user or request.user.is_staff
    
class CustomReviewPermission(permissions.BasePermission):
    """
    Custom permission to allow:
    - Anyone to read (GET)
    - Authenticated users to create (POST)
    - Owners to update (PATCH)
    - Admins to delete (DELETE)
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'PATCH', 'DELETE']:
            return request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE']:
            return obj.user == request.user or request.user.is_staff
        return False

# class IsOwnerProfilePermission(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ["PATCH", "DELETE"]:
#             return obj.user == request.user or request.user.is_staff
#         return False