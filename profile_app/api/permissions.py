from rest_framework.permissions import BasePermission, IsAuthenticated
from reviews_app.api.permissions import GenericAPIException
from profile_app.models import Profile

class IsProfileOwner(BasePermission):
    def has_permission(self, request, view):
        return True
        # if request.method in ['GET', 'PATCH']:
        #     return request.user.is_authenticated
        # raise GenericAPIException(detail="Unauthorized. The user must be authenticated.", status_code=401)

    def has_object_permission(self, request, obj):      
        if request.method == "PATCH":
            object_data = obj
            print("OBJECT DATA", object_data)
            # pk = self.context['view'].kwargs["pk"]
            pk = self.kwargs["pk"]
            pk2 = self.kwargs.get('pk')
            print("PRIVATE KEY", pk, pk2)
            # user = self.context['request'].user
            # current_profile = Profile.objects.filter(user=request.user)
            user_profile = Profile.objects.filter(user=3).values()       
            if user_profile[0]["id"] != 1:  
                raise GenericAPIException(detail="Authenticated user is not the owner of the profile", status_code=403)
            return True
        