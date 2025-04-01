from reviews_app.models import Review
from rest_framework import serializers
from profile_app.models import Profile
from datetime import datetime

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ["id", "auth_user"]
       
    def create(self, data):
        user = self.context['request'].user
        customer_profile = Profile.objects.filter(user=user).exists()
        print("POST DATEN", data)

        if customer_profile:
            profile = Profile.objects.filter(user=user)
            if profile['type'] == "customer":
                if Review.objects.filter(business_user=data['business_user']):
                    return serializers.ValidationError("You have already created a review for this business user.")
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
            return serializers.ValidationError("Only users with a customer profile are able to create a review.")

    def update(self, data, obj):
        user = self.context['request'].user
        rating = data['rating']
        description = data['description']       
        
        print("DATAAAAAA", data)
        
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




