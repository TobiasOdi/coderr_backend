from profile_app.models import Profile
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        # exclude = "auth_user"
        
    def get_object(self, user_id):
        try:
            profile = Profile.objects.get(user=user_id)
            # permission_classes = [IsOwnerOrAdmin]
            #self.check_object_permissions(self.request, obj)

            return Response(profile, status=status.HTTP_200_OK)
        except "ProfileDoesNotExist":
            raise Response(status=status.HTTP_200_OK)
