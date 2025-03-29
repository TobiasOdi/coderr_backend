from rest_framework import generics
from profile_app.models import Profile
from profile_app.api.serializers import ProfileSerializer, ListCustomerSerializer, ListBusinessSerializer
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

class ProfileInfoView(generics.RetrieveUpdateAPIView):
    """ Retrieves the detailed information of a user profile (for both customer and business users). Also allows editing of profile data (PATCH). 
        Allows a user to update certain profile information. 
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for user in self.lookup_field:
            filter["user"] = self.kwargs["pk"]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
    
class ListAllCustomer(generics.ListAPIView):
    """ Returns a list of all customer profiles on the platform. 
    """
    queryset = Profile.objects.filter(type="customer")
    serializer_class = ListCustomerSerializer
    authentication_classes = [TokenAuthentication]
    
class ListAllBusiness(generics.ListAPIView):
    """ Returns a list of all business users on the platform.
    """
    queryset = Profile.objects.filter(type="business")
    serializer_class = ListBusinessSerializer
    authentication_classes = [TokenAuthentication]


