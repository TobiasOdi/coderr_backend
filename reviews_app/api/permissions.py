from rest_framework import permissions
from offers_app.api.permissions import GenericAPIException
from profile_app.models import Profile

# class IsOwnerOrAdmin(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.user == request.user or request.user.is_staff
    
class ReviewListCreatePermission(permissions.BasePermission):
    """
    Custom permission to allow:
    - Anyone to read (GET)
    - Authenticated users to create (POST)
    - Owners to update (PATCH)
    - Admins to delete (DELETE)
    """

    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        if request.method in ['POST', 'PATCH', 'DELETE']:
            return request.user.is_authenticated
        raise GenericAPIException(detail="Unauthorized. The user must be authenticated.", status_code=401)


    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            # user = self.context['request'].user
            # current_profile = Profile.objects.filter(user=request.user)
            current_profile = Profile.objects.filter(user=15).values()       
            if current_profile[0]["type"] != "customer":  
                raise GenericAPIException(detail="Unauthorized. The user must be authenticated and have a customer profile.", status_code=401)
            
            return True
        
        if request.method in ['PATCH', 'DELETE']:
            return obj.user == request.user or request.user.is_staff
        raise GenericAPIException(detail="Forbidden. The user is not authorized to edit this rating.", status_code=403)



    # def has_permission(self, request, obj):
    
        
    #     if request.method == "POST":
    #         print("METHOD POST")
    #         # user = self.context['request'].user
    #         # current_profile = Profile.objects.filter(user=request.user)
    #         current_profile = Profile.objects.filter(user=15).values()       
    #         if current_profile[0]["type"] != "customer":  
    #             raise GenericAPIException(detail="Authenticated user is not a 'business' profile", status_code=403)
            
    #         return True


# class IsOwnerProfilePermission(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ["PATCH", "DELETE"]:
#             return obj.user == request.user or request.user.is_staff
#         return False