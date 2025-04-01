from offers_app.models import Offer, UserDetails, OfferDetails
from profile_app.models import Profile
from reviews_app.models import Review
from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:        
        model = UserDetails
        exclude = ["id", "user"]
        
class OfferDetailsSerializer(serializers.ModelSerializer):   
    class Meta:        
        model = UserDetails
        exclude = ["offer"]

class OfferSerializer(serializers.ModelSerializer):
    # details = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    # user_details = UserDetailsSerializer()
    
    class Meta:        
        model = Offer
        fields = "__all__"
               
    def create(self, data):
        user = self.context['request'].user
        profile = Profile.objects.filter(user=15).values()
        print("PROFILE", profile[0]["type"])
        if profile[0]["type"] != "business":    
            return serializers.ValidationError("Only users with a customer profile are able to create a review.")
        else:
            return data
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

