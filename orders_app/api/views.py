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
from rest_framework import status
from rest_framework.response import Response


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

class UpdateAndDeleteOrder(generics.RetrieveUpdateDestroyAPIView):
    """ Updates the status of a specific order. Possible status values are e.g. 'in_progress', 'completed', or 'canceled'.
        Deletes a specific order. This action is restricted to admin users (staff).
    """    
    # permission_classes = [IsAuthenticatedPermission, ListCreateOrderPermission]
    serializer_class = OrderSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        order = Order.objects.get(pk=pk)
        return order

# class OrdersInProgress(generics.ListAPIView):
#     """ This endpoint returns the number of orders in progress for a specific business user. Current orders are those with the status 'in_progress'.
#     """
#     # permission_classes = [IsAuthenticatedPermission, ListCreateOrderPermission]
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         queryset = Order.objects.all()

#         orders_in_progress = queryset.filter(user=int(creator_id))

#         return queryset.filter(user=int(creator_id))
class OrdersInProgress(APIView):
    """ This endpoint returns the number of orders in progress for a specific business user. Current orders are those with the status 'in_progress'.
    """
    # permission_classes = [IsAuthenticatedPermission, ListCreateOrderPermission]
       
    def get(self, request, pk):
        # pk = self.kwargs.get('pk')  
        b_user = User.objects.get(pk=pk)     
        order_count = Order.objects.filter(business_user=b_user, status="in_progress").count()
        return Response({"order_count": order_count}, status=status.HTTP_200_OK) 
 

class OrdersCompleted(APIView):
    """Returns the number of completed orders for a specific business user. Completed orders have the status 'completed'.
    """
    # permission_classes = [IsAuthenticatedPermission, ListCreateOrderPermission]

    def get(self, request, pk):
        # pk = self.kwargs.get('pk')  
        b_user = User.objects.get(pk=pk)     
        order_count = Order.objects.filter(business_user=b_user, status="completed").count()
        return Response({"order_count": order_count}, status=status.HTTP_200_OK) 
