from django.contrib.auth import authenticate,login
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json
from django.contrib.auth.models import User
from authentication_app.functions import *
from profile_app.models import Profile
from reviews_app.models import Review
from offers_app.models import Offer
from django.db.models import Avg


class RegistrationView(APIView):
    def post(self, request, format=None):
        """ Registers a new user and returns the token, username, email and user_id. Checks if the user (email) already exist, if not the user is created. If the user already exists, a HTTP 400 error is retuned.
        Args:
            request (json): Form data
        """
        new_user_Data = json.loads(request.body)
        get_user_obj = User.objects.filter(username=new_user_Data['email']).exists()
        if new_user_Data['password'] != new_user_Data['repeated_password']:
            return Response( status=status.HTTP_400_BAD_REQUEST)
        else:
            if get_user_obj:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                new_user_id_token = create_new_user_object(new_user_Data) 
                  
                return Response(
                    {   "token": str(new_user_id_token[1]),
                        "username": new_user_Data['username'], 
                        "email": new_user_Data['email'], 
                        "user_id": new_user_id_token[0]
                    }, status=status.HTTP_201_CREATED)
        
class LoginView(APIView):
    def post(self, request, format=None):
        """ Logs the user into his account and returns the token, username, email and user_id. A HTTP 400 error is retuned if credentials are incorrect or user does not exist.
        Args:
            request (json): Form data
        """
        login_Data = json.loads(request.body)
        user = authenticate(request, username=login_Data['username'], password=login_Data['password'])
        get_user_obj = User.objects.filter(pk=user.pk).exists()
        if get_user_obj:
            if user:
                token = Token.objects.get(user=user)
                login(request, user)
                return Response({"token": str(token), "username": user.username, "email": user.email, "user_id": user.id}, 
                                status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class BaseInfoView(APIView):
    """ Retrieves general basic information about the platform, including the number of reviews, the average review score, the number of 
    business users and the number of listings. 
    """    
    def get(self, request, format=None):
        reviews_av_rating = Review.objects.all().aggregate(Avg("rating"))
        if reviews_av_rating["rating__avg"] == None:
            reviews_av_rating = "-"
        else:
            round(reviews_av_rating["rating__avg"], 1)
        offers = Offer.objects.all().count()
        rev_count = Review.objects.all().count()
        aver_rating = reviews_av_rating
        buss_profile_count = Profile.objects.filter(type="business").count()
        print(buss_profile_count)
        offer_count = offers
        return Response({"review_count": rev_count, "average_rating": aver_rating, "business_profile_count": buss_profile_count, "offer_count": offer_count},
                        status=status.HTTP_200_OK)      
