from django.db import models
from django.contrib.auth.models import User

USER_TYPE = {
    "customer": "customer",
    "business": "business",
}
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    type = models.CharField(max_length=50, choices=USER_TYPE,blank=False)
    username = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=False)
    file = models.CharField(max_length=50, black=True)

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    type = models.CharField(max_length=50, choices=USER_TYPE,blank=False)
    username = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=False)
    file = models.CharField(max_length=50, black=True)
    location = models.CharField(max_length=50, black=True)
    tel = models.CharField(max_length=50, black=True)
    description = models.CharField(max_length=200, black=True)
    working_hours = models.CharField(max_length=50, black=True)

