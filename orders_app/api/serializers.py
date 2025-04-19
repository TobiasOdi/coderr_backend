from orders_app.models import Order
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
from datetime import datetime

class OrderSerializer(serializers.ModelSerializer):
    offer_detail_id = serializers.IntegerField()
    
    class Meta:        
        model = Order
        exclude = ["detail"]

    def create(self, validated_data):
        print("DATAAAAA", validated_data)
        offer_details = Details.objects.filter(pk=validated_data["offer_detail_id"])
        offer_details_instance = Details.objects.get(pk=validated_data["offer_detail_id"])
        offer_details_values = offer_details.values()
        offer_data = Offer.objects.filter(pk=offer_details_values[0]["offer_id"])
        offer_values = offer_data.values()
        business_user = User.objects.get(pk=offer_values[0]["user_id"])
        # user = self.request.user
        user = User.objects.get(pk=7)
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")


        new_order = Order.objects.create(
            customer_user=user,
            business_user=business_user,
            detail = offer_details_instance,
            offer_detail_id = validated_data["offer_detail_id"],
            title=offer_details_values[0]["title"],
            revisions=offer_details_values[0]["revisions"],
            delivery_time_in_days=offer_details_values[0]["delivery_time_in_days"],
            price=offer_details_values[0]["price"],
            features=offer_details_values[0]["features"],
            offer_type=offer_details_values[0]["offer_type"],
            status="in_progress",
            created_at=dt_string,
            updated_at=dt_string
        )
        return new_order




