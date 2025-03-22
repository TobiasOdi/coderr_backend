from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json
from django.contrib.auth.models import User
from authentication_app.functions import *


class RegistrationView(APIView):
    def post(self, request, format=None):
        """ Checks if the username (email) already exist, if not the user is created. If the username already exists, it returns a json with the status 1.
        Args:
            request (json): New user data
        """
        newUserData = json.loads(request.body)
        get_user_obj = User.objects.filter(username=newUserData['email']).exists()
        if newUserData['password'] != newUserData['repeated_password']:
            return Response( status=status.HTTP_400_BAD_REQUEST)
        else:
            if get_user_obj:
                return Response( status=status.HTTP_400_BAD_REQUEST)
            else:          
                createObjectsForNewUser(newUserData)
                return Response(
                    {
                        "token": "83bf098723b08f7b23429u0fv8274",
                        "username": "exampleUsername",
                        "email": "example@mail.de",
                        "user_id": 123
                    }, status=status.HTTP_201_CREATED)
        
class LoginView(APIView):
    pass
