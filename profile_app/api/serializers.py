from profile_app.models import Profile
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        # exclude = "auth_user"