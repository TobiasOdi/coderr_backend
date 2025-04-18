from offers_app.models import Offer, Details
from profile_app.models import Profile
from reviews_app.models import Review
from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from offers_app.api.functions import CustomValidation
from rest_framework import status
import json
from django.db.models import Min
        
class DetailsSerializer(serializers.ModelSerializer):  
    class Meta:        
        model = Details
        fields = "__all__"

class OffersSerializer(serializers.ModelSerializer):
    details = DetailsSerializer(many=True, read_only=True)
    # details = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="ListAndCreateOffer")
    min_price = serializers.SerializerMethodField('min_price_calc')
    min_delivery_time = serializers.SerializerMethodField('min_delivery_time_calc')

    class Meta:        
        model = Offer
        fields = ["id", "user", "title", "image", "description", "created_at", "updated_at", "details", "min_price", "min_delivery_time"]

    def min_price_calc(self, obj): 
        price = Details.objects.filter(offer=obj.pk).aggregate(Min("price", default=0))
        return price["price__min"]

    def min_delivery_time_calc(self, obj):
        time = Details.objects.filter(offer=obj.pk).aggregate(Min("delivery_time_in_days", default=0))     
        return time["delivery_time_in_days__min"]
     
class OfferListSerializer(OffersSerializer):
    # details = serializers.HyperlinkedIdentityField(view_name="details-list", lookup_url_kwarg='offer_pk')
    user_details = serializers.SerializerMethodField('get_user_details')
    
    class Meta:        
        model = Offer
        fields = ["id", "user", "title", "image", "description", "created_at", "updated_at", "details", "min_price", "min_delivery_time", "user_details"]

    def get_user_details(self, obj):
        # user = self.context['request'].user
        user_data = {
        "first_name": "Tobias",
        "last_name": "Odermatt",
        "username": "Tobias Geschäft"
        }
        return user_data

class OfferSerializer(serializers.ModelSerializer):
    details = DetailsSerializer(many=True)  
    class Meta:        
        model = Offer
        fields = ["title", "image", "description", "details"]
           
    def create(self, data): 
        offer_details = data['details']
        offer_data = data
        try:
            del offer_data['details']
        except KeyError as ex:
            print("No such key: '%s'" % ex.message)
        offer = Offer.objects.create(**data)
        batch = [Details(offer=offer,
                              title=row['title'], 
                              revisions=row['revisions'], 
                              delivery_time_in_days=row['delivery_time_in_days'], 
                              price=row['price'], 
                              features=row['features'], 
                              offer_type=row['offer_type']) for row in offer_details]
        Details.objects.bulk_create(batch)
        return offer

class OfferDetailSerializer(OffersSerializer):
    details = DetailsSerializer(many=True, read_only=True)

    class Meta:        
        model = Offer
        fields = ["id", "user", "title", "image", "description", "created_at", "updated_at", "details", "min_price", "min_delivery_time"]

class OfferDetailPatchDeleteSerializer(OffersSerializer):
    details = DetailsSerializer(many=True, read_only=True)

    class Meta:        
        model = Offer
        fields = ["id", "title", "image", "description", "details"]
        
    def update(self, data, obj):
        pk = self.context['view'].kwargs["pk"]
        print("DATAAAA", obj)
        offer_details = obj['details']
        offer_data = obj
        try:
            del offer_data['details']
        except KeyError as ex:
            print("No such key: '%s'" % ex.message)
        updated_offer = Offer.objects.update(offer_data)

        
        
        
        
        print("updated_offer",updated_offer)

        offer_details = Details.objects.filter(offer=pk)
        print("offer_details",offer_details)

    
class DetailItemSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Details
        fields = "__all__"
    
    
    
    
    
    
    
    
    
    

    # def destroy(self, data, obj):
    #     user = self.context['request'].user
    #     rating = data['rating']
    #     description = data['description']
        
    #     if obj.user == user.pk:
    #             raise serializers.ValidationError("You cannot delete this review, because you are not the owner.")
    #     return data
