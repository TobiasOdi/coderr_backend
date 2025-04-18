from profile_app.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["id", "uploaded_at"]
        
class ListBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user", "username", "first_name", "last_name", "file", "location", "tel", "description", "working_hours", "type"]
        
class ListCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "username", "first_name", "last_name", "file", "uploaded_at", "type"]