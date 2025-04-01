from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=13) 
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)

class OfferDetails(models.Model):
    # offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True) 
    title = models.CharField(max_length=50)
    revisions = models.IntegerField()
    delivery_time_in_days = models.IntegerField()
    price = models.IntegerField()
    features = models.CharField(max_length=200)
    offer_type = models.CharField(max_length=25)
   
class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=15) 
    title = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=25, null=True, blank=True)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.CharField(max_length=50, blank=True, editable=False)
    updated_at = models.CharField(max_length=50, blank=True, editable=False)
    details = models.CharField(max_length=50, null=True, blank=True)
    min_price = models.IntegerField(blank=True, null=True)
    min_delivery_time = models.IntegerField(blank=True, null=True)
    
    # user_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE)


