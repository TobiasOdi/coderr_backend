from django.db import models
from django.contrib.auth.models import User
from profile_app.models import Profile


class Review(models.Model):
    business_user = models.OneToOneField(Profile, on_delete=models.CASCADE, default=7) 
    reviewer = models.OneToOneField(User, on_delete=models.CASCADE, default=1) 
    rating = models.IntegerField(null=True, blank=False)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.CharField(max_length=50, blank=False, default="2023-10-30T10:00:00Z")
    updated_at = models.CharField(max_length=50, null=True, blank=True)
    
    # def __str__(self):
    #     return f"{self.user}"

