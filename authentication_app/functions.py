from django.contrib.auth.models import User
from profile_app.models import CustomerProfile, BusinessProfile

def createObjectsForNewUser(newUserData):
    new_user = User.objects.create_user(
        username=newUserData['username'],
        password=newUserData['password'],
        email=newUserData['email'],
    )
    new_user.set_password(newUserData['password'])
    new_user.save()
    
    if newUserData['type'] == "customer":
        CustomerProfile.objects.create(
            user=new_user,
            type="customer",
            username=newUserData['username'],
            first_name="",
            last_name="",
            email=newUserData['email'],
            file=""
        )
    elif newUserData['type'] == "business": 
        BusinessProfile.objects.create(
            user=new_user,
            type="business",
            username=newUserData['username'],
            first_name="",
            last_name="",
            email=newUserData['email'],
            file="",
            location="",
            tel="",
            description="",
            working_hours=""
        )
