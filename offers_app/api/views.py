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

# Create your views here.
class ListAndCreateOffer(generics.ListCreateAPIView):
    """ This endpoint returns a list of offers. Each offer contains an overview of the offer details, the minimum price and the shortest delivery time.
        This end point makes it possible to create a new offer.
    """
    # permission_classes = [IsAuthenticatedPermission, ListCreateOfferPermission]
    ordering_fields = ['updated_at', 'min_price']
    search_fields = ['title', 'description', 'user__first_name', 'user__last_name']
    pagination_class = LargeResultSetPagination
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OfferListSerializer
        else:
            return OfferSerializer
    
    def get_queryset(self):
        queryset = Offer.objects.all()
        queryset = filtered_queryset(self, queryset)
        return queryset
                
    def perform_create(self, serializer):
        # print("SERIALIZER", serializer.data)
        additional_field_data = get_additional_field_data(self)
        serializer.save(
            user=additional_field_data["user"],
            created_at=additional_field_data["date"],
            updated_at=additional_field_data["date"],
        )

class OfferDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """ This endpoint returns the details of a specific offer based on the specified ID.
        Updates a specific offer. A PATCH only overwrites the specified fields. Not all fields need to be specified, only those that are to be updated.
        Löscht ein spezifisches Angebot anhand der angegebenen ID. 
    """
    
    # permission_classes = [ListCreateOfferPermission]   

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OfferDetailSerializer
        elif self.request.method in ['PATCH', 'DELETE']:
            return OfferDetailPatchDeleteSerializer
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        offer = Offer.objects.get(pk=pk)
        return offer
        
        
class OfferDetailItem(generics.RetrieveAPIView):
    # permission_classes = [ListCreateOfferPermission]   
    serializer_class = DetailItemSerializer
    def get_object(self):
        pk = self.kwargs.get('pk')
        print("PK", pk)
        offer_detail = Details.objects.get(pk=pk)
        return offer_detail
        