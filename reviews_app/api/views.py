from django.shortcuts import render
from rest_framework import generics
from reviews_app.models import Review
from reviews_app.api.serializers import ReviewSerializer
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class ListAllReviews(generics.ListCreateAPIView):
    """ Lists all available ratings. The reviews can be sorted by 'updated_at' or 'rating'.
        Filter parameters such as 'business_user_id' and 'reviewer_id' can also be used. 
    """
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
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