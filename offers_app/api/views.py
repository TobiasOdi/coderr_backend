from rest_framework import generics
from offers_app.models import Offer
from offers_app.api.serializers import ListOfferSerializer, OfferSerializer
from rest_framework.authentication import TokenAuthentication
import json
from django.shortcuts import get_object_or_404
from offers_app.api.permissions import ListCreateOfferPermission
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.
class ListAndCreateOffer(generics.ListCreateAPIView):
    """ This endpoint returns a list of offers. Each offer contains an overview of the offer details, the minimum price and the shortest delivery time.
        This end point makes it possible to create a new offer.
    """
    #   permission_classes = [ListCreateOfferPermission]
    ordering_fields = ['updated_at', 'min_price']
    search_fields = ['title', 'description', 'user__first_name', 'user__last_name']
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListOfferSerializer
        return OfferSerializer

    
    def get_queryset(self):
        queryset = Offer.objects.all()
        creator_id = self.request.query_params.get('creator_id')
        min_price = self.request.query_params.get('min_price')
        max_delivery_time = self.request.query_params.get('max_delivery_time')

        if creator_id is not None:
            queryset = queryset.filter(business_user=creator_id)
        if min_price is not None:
            queryset = queryset.filter(min_price__egt=min_price)
        if max_delivery_time is not None:
            queryset = queryset.filter(min_delivery_time__lte=max_delivery_time)
        return queryset
    
    def perform_create(self, serializer):
        print("SERIALIZER", serializer)
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")

        u = User.objects.get(pk=15)
        serializer.save(
            user=u,
            created_at=dt_string,
            updated_at=dt_string,
        )
        
        # print("NEW OFFER", new_offer.id)
        
        # currentTask = json.loads(request.body)      
        # subtaskData = currentTask[0]['subtaskData']
        # newTask = createNewTask(taskData, request)      
        # for subtask in subtaskData: 
        #     SubtaskItem.objects.create(
        #         parent_task_id=newTask,
        #         status=subtask['status'], 
        #         subtaskName=subtask['subtaskName']
        #     )
        
        
        
        # serializer.save(user=self.request.user)

class OfferDetailUpdateDelete(generics.ListCreateAPIView):
    """ This endpoint returns a list of offers. Each offer contains an overview of the offer details, the minimum price and the shortest delivery time.
        This end point makes it possible to create a new offer.
    """
    serializer_class = OfferSerializer
    permission_classes = [ListCreateOfferPermission]
    ordering_fields = ['updated_at', 'min_price']
    search_fields = ['title', 'description', 'user__first_name', 'user__last_name']
    
    
    def get_queryset(self):
        queryset = Offer.objects.all()
        creator_id = self.request.query_params.get('creator_id')
        min_price = self.request.query_params.get('min_price')
        max_delivery_time = self.request.query_params.get('max_delivery_time')

        if creator_id is not None:
            queryset = queryset.filter(business_user=creator_id)
        if min_price is not None:
            queryset = queryset.filter(min_price__egt=min_price)
        if max_delivery_time is not None:
            queryset = queryset.filter(min_delivery_time__lte=max_delivery_time)
        return queryset
    
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
        
        
    
    # def get_queryset(self):
    #     return RackItem.objects.filter(shopper=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.DATA)

    #     if not serializer.is_valid():
    #         return Response(
    #             serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     item = RackItem.objects.create(
    #         shopper=request.user,
    #         item_url=serializer.data['item_url'],
    #         item_image_url=serializer.data['item_image_url'])

    #     result = RackItemSerializer(item)
    #     return Response(result.data, status=status.HTTP_201_CREATED)    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# class UpdateDeleteOwnReview(generics.RetrieveUpdateDestroyAPIView):
#     """ Updates selected fields of an existing rating (only 'rating' and 'description' are editable). The endpoint allows the creator of the 
#         rating to edit the rating.
#     """
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [CustomReviewPermission]

#     def get_object(self):
#         queryset = self.get_queryset()
#         filter = {}
#         for id in self.lookup_field:
#             filter["id"] = self.kwargs["review_id"]
#         obj = get_object_or_404(queryset, **filter)
#         self.check_object_permissions(self.request, obj)
#         return obj or {}
        

