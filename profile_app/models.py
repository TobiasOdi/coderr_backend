from django.db import models
from django.contrib.auth.models import User

USER_TYPE = {
    "customer": "customer",
    "business": "business",
}
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False, editable=False, default=13)
    username = models.CharField(max_length=50, blank=False, editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    file = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    working_hours = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, choices=USER_TYPE, blank=False, editable=False)
    email = models.EmailField(max_length=50, blank=True)
    created_at = models.CharField(max_length=50, blank=True, editable=False)
    uploaded_at = models.CharField(max_length=200, blank=True)

