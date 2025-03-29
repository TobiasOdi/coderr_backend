from django.db import models
from django.contrib.auth.models import User
from profile_app.models import Profile


class Review(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    business_user = models.IntegerField(blank=True)
    reviewer = models.IntegerField(blank=True) 
    rating = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.CharField(max_length=50, blank=True)
    updated_at = models.CharField(max_length=50, null=True, blank=True)
    

