from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from profile_app.models import Profile
from profile_app.api.serializers import ProfileSerializer
from rest_framework.authentication import TokenAuthentication

class ProfileInfoView(generics.RetrieveUpdateAPIView):
    authenticaiton_classes = [TokenAuthentication]
    """ Ruft die detaillierten Informationen eines Benutzerprofils ab (sowohl für Kunden- als auch für Geschäftsnutzer). Ermöglicht auch das Bearbeiten der Profildaten (PATCH). 
        Ermöglicht es einem Benutzer, bestimmte Profilinformationen zu aktualisieren. 
    """
    queryset = Profile.objects.all()
    print("Queryset", queryset)
    serializer_class = ProfileSerializer


    # new_user_Data = json.loads(request.body)
    # get_user_obj = User.objects.filter(username=new_user_Data['email']).exists()
    # if new_user_Data['password'] != new_user_Data['repeated_password']:
    #     return Response( status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     if get_user_obj:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         new_user_id_token = createObjectsForNewUser(new_user_Data)               
    #         return Response(
    #             {
    #                 "user": 1,
    #                 "username": "max_mustermann",
    #                 "first_name": "Max",
    #                 "last_name": "Mustermann",
    #                 "file": "profile_picture.jpg",
    #                 "location": "Berlin",
    #                 "tel": "123456789",
    #                 "description": "Business description",
    #                 "working_hours": "9-17",
    #                 "type": "business",
    #                 "email": "max@business.de",
    #                 "created_at": "2023-01-01T12:00:00"
    #             }, status=status.HTTP_200_OK)
