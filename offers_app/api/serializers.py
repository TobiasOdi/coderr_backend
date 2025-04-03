from offers_app.models import Offer, UserDetails, OfferDetails
from profile_app.models import Profile
from reviews_app.models import Review
from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
import json

class UserDetailsSerializer(serializers.ModelSerializer):
    features = serializers.JSONField()
    class Meta:        
        model = UserDetails
        exclude = ["id", "user"]
        
class OfferDetailSerializer(serializers.ModelSerializer):   
    class Meta:        
        model = OfferDetails
        # exclude = ["offer"]
        fields = "__all__"


class ListOfferSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Offer
        fields = "__all__"



class OfferSerializer(serializers.ModelSerializer):
    # created_at=serializers
    # updated_at=dt_string
    details = OfferDetailSerializer(many=True)
    # details = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    # user_details = UserDetailsSerializer()
    
    class Meta:        
        model = Offer
        fields = ["title", "image", "description", "details"]
        
    # def validate_details(self, data):
    #     print("DATA", data)
    #     # print("REQUEST DATA", request_data)   
    #     # subtaskData = currentTask[0]['subtaskData']

    #     details = OfferDetails.objects.create()
               
    def create(self, data):
        user = self.context['request'].user
        profile = Profile.objects.filter(user=15).values()
        print("PROFILE", profile[0]["type"])
        if profile[0]["type"] != "business":    
            return serializers.ValidationError("Only users with a business profile are able to create an offer.")
        else:
            # print("DETAILS DATA", data['details']['features'])
            offer = Offer.objects.create(**data)
            # details_data = data.pop('details')
            # details = OfferDetails.objects.create(**data['details'])
            # offer.details.set(details)
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

