from django.contrib.auth.models import User
from profile_app.models import Profile
from rest_framework.authtoken.models import Token
from datetime import datetime


def createObjectsForNewUser(newUserData):
    new_user = User.objects.create_user(
        username=newUserData['username'],
        password=newUserData['password'],
        email=newUserData['email'],
    )
    new_user.set_password(newUserData['password'])
    new_user.save()
    token, created = Token.objects.get_or_create(user=new_user)
    
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")

    Profile.objects.create(
        auth_user=new_user,
        user=new_user.pk,
        type=newUserData["type"],
        username=newUserData['username'],
        first_name="",
        last_name="",
        email=newUserData['email'],
        file="",
        location="",
        tel="",
        uploaded_at="",
        description="",
        working_hours="",
        created_at=dt_string
    )

    return [new_user.id, token]
