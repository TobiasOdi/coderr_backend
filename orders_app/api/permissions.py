from rest_framework import permissions
from profile_app.models import Profile
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from offers_app.models import Offer


class GenericAPIException(APIException):
    """
    raises API exceptions with custom messages and custom status codes
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'error'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


# class IsOwnerOrAdmin(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.user == request.user or request.user.is_staff

class IsAuthenticatedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
         if request.method == "GET":
             print("AUTHENTIFIZIERT", request.user.is_authenticated)
             return request.user.is_authenticated
         return Response("User is not authenticated.", status=status.HTTP_401_UNAUTHORIZED)


class ListCreateOrderPermission(permissions.BasePermission):
    """
    Custom permission to allow:
    - Anyone to read (GET)
    - Authenticated users to create (POST)
    - Owners to update (PATCH)
    - Admins to delete (DELETE)
    """

    def has_object_permission(self, request, obj):       
        if request.method == "POST":
            print("METHOD POST")
            user = request.user
            # current_profile = Profile.objects.filter(user=request.user)
            current_profile = Profile.objects.filter(user=user).values() 
            print("CURRENT PROFILE", current_profile)      
            if current_profile[0]["type"] != "business":  
                raise GenericAPIException(detail="Authenticated user is not a 'business' profile", status_code=403)
            
            return True
        
        if request.method in ['PATCH', 'DELETE']:
            offer_id = request.resolver_match.kwargs.get('offer_id')
            offer = Offer.objects.filter(pk=offer_id).values()
            if offer[0]["user"] != request.user:
                raise GenericAPIException(detail="Authenticated user is not the owner of the offer", status_code=403)
            return True


    
# class IsOwnerOfferPermission(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ["PATCH", "DELETE"]:
#             return obj.user == request.user or request.user.is_staff
#         return False

# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

# class StandardResultsSetPagination(LimitOffsetPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
