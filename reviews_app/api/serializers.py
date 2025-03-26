from reviews_app.models import Review
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ["id", "auth_user"]

