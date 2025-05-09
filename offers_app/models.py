from django.db import models
from django.contrib.auth.models import User
   
class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=15) 
    title = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=25, null=True, blank=True)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.CharField(max_length=50, blank=True, editable=False)
    updated_at = models.CharField(max_length=50, blank=True, editable=False)
    min_price = models.IntegerField(blank=True, null=True)
    min_delivery_time = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Details(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="details", null=True) 
    title = models.CharField(max_length=50, blank=True, null=True)
    revisions = models.IntegerField()
    delivery_time_in_days = models.IntegerField()
    price = models.IntegerField()
    features = models.JSONField()
    offer_type = models.CharField(max_length=25)

    def __str__(self):
        return self.title
    
class UserDetails(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="user_details", null=True) 
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)




