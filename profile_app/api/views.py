from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from profile_app.models import Profile
from profile_app.api.serializers import ProfileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import json


class ProfileInfoView(generics.RetrieveUpdateAPIView):
    authenticaiton_classes = [TokenAuthentication]
    """ Ruft die detaillierten Informationen eines Benutzerprofils ab (sowohl für Kunden- als auch für Geschäftsnutzer). Ermöglicht auch das Bearbeiten der Profildaten (PATCH). 
        Ermöglicht es einem Benutzer, bestimmte Profilinformationen zu aktualisieren. 
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        print("QUERYSET", queryset)
        filter = {}
        for user in self.lookup_field:
            filter["user"] = self.kwargs["pk"]

        obj = get_object_or_404(queryset, **filter)
        print("OBJECT", obj)
        self.check_object_permissions(self.request, obj)
    
        return obj


