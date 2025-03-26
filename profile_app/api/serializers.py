from profile_app.models import Profile
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["id", "auth_user"]

class ListCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "username", "first_name", "last_name", "file", "uploaded_at", "type"]
        
class ListBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "username", "first_name", "last_name", "file", "location", "tel", "description", "working_hours", "type"]