from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from profile_app.models import Profile
from profile_app.api.serializers import ProfileSerializer, ListCustomerSerializer, ListBusinessSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import json
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class ProfileInfoView(generics.RetrieveUpdateAPIView):
    """ Ruft die detaillierten Informationen eines Benutzerprofils ab (sowohl für Kunden- als auch für Geschäftsnutzer). Ermöglicht auch das Bearbeiten der Profildaten (PATCH). 
        Ermöglicht es einem Benutzer, bestimmte Profilinformationen zu aktualisieren. 
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
    """ Gibt eine Liste aller Geschäftsnutzer auf der Plattform zurück. 
    """
    queryset = Profile.objects.filter(type="customer")
    serializer_class = ListCustomerSerializer
    authentication_classes = [TokenAuthentication]
    
class ListAllBusiness(generics.ListAPIView):
    """ Gibt eine Liste aller Kundenprofile auf der Plattform zurück.  
    """
    queryset = Profile.objects.filter(type="business")
    serializer_class = ListBusinessSerializer
    authentication_classes = [TokenAuthentication]


