from django.db import models
from django.contrib.auth.models import User

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    title = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=25, blank=True)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.CharField(max_length=50, blank=True, editable=False)
    updated_at = models.CharField(max_length=50, blank=True, editable=False)
    min_price = models.IntegerField(blank=True, null=True),
    min_delivery_time = models.IntegerField(blank=True, null=True)

class OfferDetail(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True) 
    url = models.CharField(max_length=50, blank=True) 

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)