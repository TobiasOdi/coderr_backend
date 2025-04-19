from django.db import models
from django.contrib.auth.models import User
from offers_app.models import Details

USER_TYPE = {
    "in_progress": "in_progress",
    "completed": "completed",
    "cancelled": "cancelled"
}

class Order(models.Model):
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="customer_user")
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="business_user")
    detail = models.ForeignKey(Details, on_delete=models.CASCADE, blank=True, null=True)
    offer_detail_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True)
    revisions = models.IntegerField(null=True)
    delivery_time_in_days = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    features = models.JSONField(null=True)
    offer_type = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=15, choices=USER_TYPE, blank=False, editable=False)
    created_at = models.CharField(max_length=50, blank=True, editable=False)
    updated_at = models.CharField(max_length=50, blank=True, editable=False)

    def __str__(self):
        return self.title


