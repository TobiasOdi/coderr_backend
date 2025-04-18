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

class OrderSerializer(serializers.ModelSerializer):
    offer_detail_id = serializers.IntegerField()
    class Meta:        
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        print("DATAAAAA", validated_data)
        offer_details = Details.objects.filter(pk=validated_data["offer_detail_id"])
        offer_details_values = offer_details.values()
        offer_data = Offer.objects.filter(pk=offer_details_values[0]["offer_id"])
        offer_values = offer_data.values()
        business_user = User.objects.get(pk=offer_values[0]["user_id"])
        
        # user = self.request.user
        user = User.objects.get(pk=4)

        new_order = Order.objects.create(
            customer_user=user,
            business_user=business_user,
            title=offer_details_values[0]["title"],
            revisions=offer_details_values[0]["revisions"],
            delivery_time_in_days=offer_details_values[0]["delivery_time_in_days"],
            price=offer_details_values[0]["price"],
            features=offer_details_values[0]["features"],
            offer_type=offer_details_values[0]["offer_type"],
            status="in_progress",
            created_at=offer_values[0]["created_at"],
            updated_at=offer_values[0]["updated_at"]
        )
        return new_order
