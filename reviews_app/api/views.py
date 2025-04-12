from rest_framework import generics
from reviews_app.models import Review
from reviews_app.api.serializers import ReviewSerializer
from rest_framework.authentication import TokenAuthentication
import json
from django.shortcuts import get_object_or_404
from reviews_app.api.permissions import ReviewListCreatePermission

# Create your views here.
class ListAndCreateReviews(generics.ListCreateAPIView):
    """ Lists all available ratings. The reviews can be sorted by 'updated_at' or 'rating'. Filter parameters such as 'business_user_id' 
        and 'reviewer_id' can also be used.  Creates a new review for a business user. Only authenticated users with a customer profile may 
        create reviews. A user can only submit one review per business profile.
    """
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewListCreatePermission]
    ordering_fields = ['updated_at', 'rating']
    
    def get_queryset(self):
        queryset = Review.objects.all()
        business_user_id = self.request.query_params.get('business_user_id')
        reviewer_id = self.request.query_params.get('reviewer_id')

        if business_user_id is not None:
            queryset = queryset.filter(business_user=business_user_id)
        if reviewer_id is not None:
            queryset = queryset.filter(reviewer=reviewer_id)
        return queryset
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateDeleteOwnReview(generics.RetrieveUpdateDestroyAPIView):
    """ Updates selected fields of an existing rating (only 'rating' and 'description' are editable). The endpoint allows the creator of the 
        rating to edit the rating.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewListCreatePermission]

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for id in self.lookup_field:
            filter["id"] = self.kwargs["review_id"]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj or {}
        

        