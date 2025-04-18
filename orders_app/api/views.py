from rest_framework import generics
from offers_app.models import Offer, Details
from offers_app.api.serializers import OfferListSerializer, OfferSerializer, OfferDetailSerializer, OfferDetailPatchDeleteSerializer, DetailItemSerializer
from rest_framework.authentication import TokenAuthentication
import json
from django.shortcuts import get_object_or_404
from offers_app.api.permissions import IsAuthenticatedPermission, ListCreateOfferPermission
from django.contrib.auth.models import User
from datetime import datetime
from offers_app.api.functions import filtered_queryset, get_additional_field_data
from offers_app.api.pagination import LargeResultSetPagination
from orders_app.api.serializers import OrderSerializer
from orders_app.models import Order
from profile_app.models import Profile
from rest_framework.views import APIView

class ListAndCreateOrders(generics.ListCreateAPIView):
    """ Returns a list of orders created either by the logged-in user as a customer or as a business partner.
        Creates a new order based on the details of an offer (OfferDetail).
    """

    # permission_classes = [IsAuthenticatedPermission, ListCreateOrderPermission]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        queryset = Order.objects.all()
        if self.request.method == 'GET':
            # user = self.request.user
            user = User.objects.get(pk=4)
            user_profile = Profile.objects.filter(user=user).values()
            if user_profile[0]["type"] == "customer":
                queryset = Order.objects.filter(customer_user=user.pk)
            elif user_profile[0]["type"] == "customer":
                queryset = Order.objects.filter(business_user=user.pk)
            return queryset
        else:
            return queryset


# class ListAndCreateOrders(APIView):
#     def post(self, request, format=None):

#         data = json.loads(request.body)
#         print("DATAAAAA", data)

            
    # def perform_create(self, serializer):
    #     # print("SERIALIZER", serializer.data)
    #     additional_field_data = get_additional_field_data(self)
    #     serializer.save(
    #         user=additional_field_data["user"],
    #         created_at=additional_field_data["date"],
    #         updated_at=additional_field_data["date"],
    #     )
