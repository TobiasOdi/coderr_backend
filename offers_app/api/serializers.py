from offers_app.models import Offer, UserDetails, OfferDetails
from profile_app.models import Profile
from reviews_app.models import Review
from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from offers_app.api.functions import CustomValidation
from rest_framework import status

class UserDetailsSerializer(serializers.ModelSerializer):
    features = serializers.JSONField()
    class Meta:        
        model = UserDetails
        fields = "__all__"
        
class OfferDetailsSerializer(serializers.ModelSerializer):   
    class Meta:        
        model = OfferDetails
        # exclude = ["offer"]
        fields = "__all__"


class ListOfferSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Offer
        fields = "__all__"

class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailsSerializer(many=True)  
    class Meta:        
        model = Offer
        fields = ["title", "image", "description", "details"]
           
    def create(self, data):
        user = self.context['request'].user
        profile = Profile.objects.filter(user=15).values()
        if profile[0]["type"] != "business":  
            raise CustomValidation("Authenticated user is not a 'business' profile", profile[0]["username"], status.HTTP_403_FORBIDDEN)  
        else:
            offer = Offer.objects.create(**data)
            return offer
       
        
        
    # def update(self, data, obj):
    #     user = self.context['request'].user
    #     rating = data['rating']
    #     description = data['description']       
        
    #     print("DATAAAAAA", data)
        
    #     if rating != None and description != None:
    #         if obj.reviewer == user.pk:
    #             return data
    #     else:
    #         raise serializers.ValidationError("You cannot update this review, because you are not the owner.")

    # def destroy(self, data, obj):
    #     user = self.context['request'].user
    #     rating = data['rating']
    #     description = data['description']
        
    #     if obj.reviewer == user.pk:
    #             raise serializers.ValidationError("You cannot delete this review, because you are not the owner.")
    #     return data

