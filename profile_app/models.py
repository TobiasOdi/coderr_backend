from django.db import models
from django.contrib.auth.models import User

USER_TYPE = {
    "customer": "customer",
    "business": "business",
}
class Profile(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    user = models.IntegerField(blank=False, editable=False)
    type = models.CharField(max_length=50, choices=USER_TYPE, blank=False, editable=False)
    username = models.CharField(max_length=50, blank=False, editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    file = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    uploaded_at = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    working_hours = models.CharField(max_length=50, blank=True)
    created_at = models.CharField(max_length=50, blank=True, editable=False)
