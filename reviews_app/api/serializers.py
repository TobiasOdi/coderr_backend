from reviews_app.models import Review
from rest_framework import serializers
from profile_app.models import Profile
from datetime import datetime
from offers_app.api.functions import CustomValidation
from rest_framework import status


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ["id", "auth_user"]
       
    def create(self, data):
        user = self.context['request'].user
        # customer_profile = Profile.objects.filter(user=user).exists()
        existing_review = Review.objects.filter(reviewer__iexact=user, business_user__iexact=data["business_user"]).exists()

        if existing_review:
            raise CustomValidation("You have already created a review for this business user.", user, status.HTTP_403_FORBIDDEN)  
        else:
            now = datetime.now()    
            dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
            return {
                    "business_user": data['business_user'],
                    "reviewer": user.pk, 
                    "rating": data["rating"],
                    "description": data["description"],
                    "created_at": dt_string,
                    "updated_at": dt_string
                    }

    def update(self, data, obj):
        user = self.context['request'].user
        rating = data['rating']
        description = data['description']       
        
        if rating != None and description != None:
            if obj.reviewer == user.pk:
                return data
        else:
            raise serializers.ValidationError("You cannot update this review, because you are not the owner.")

    def destroy(self, data, obj):
        user = self.context['request'].user
        rating = data['rating']
        description = data['description']
        
        if obj.reviewer == user.pk:
                raise serializers.ValidationError("You cannot delete this review, because you are not the owner.")
        return data




