from rest_framework import generics
from profile_app.models import Profile
from profile_app.api.serializers import ProfileSerializer, ListCustomerSerializer, ListBusinessSerializer
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from profile_app.api.permissions import IsProfileOwner
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProfileInfoView(generics.RetrieveUpdateAPIView):
    """ Retrieves the detailed information of a user profile (for bothHTT
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsProfileOwner]
    
    def get_object(self):
        # queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        # filter = {}
        # for user in self.lookup_field:
        #     filter["user"] = self.kwargs["pk"]
        # obj = get_object_or_404(queryset, **filter)
        # # self.check_object_permissions(self.request, obj)

        profile = Profile.objects.get(pk=pk)
        print("PROFILE", profile)
        return profile
 
    
class ListAllBusiness(generics.ListAPIView):
    """ Returns a list of all business users on the platform.
    """
    queryset = Profile.objects.filter(type="business")
    serializer_class = ListBusinessSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminForDeleteOrPatchAndReadOnly]
    
class ListAllCustomer(generics.ListAPIView):
    """ Returns a list of all customer profiles on the platform. 
    """
    queryset = Profile.objects.filter(type="customer")
    serializer_class = ListCustomerSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminForDeleteOrPatchAndReadOnly]



