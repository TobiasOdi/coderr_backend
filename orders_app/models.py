from django.db import models

class Order(models.Model):
    pass
    # user = models.OneToOneField(User, on_delete=models.CASCADE)    
    # color = models.CharField(max_length=25, blank=False, default=None)
    # text_color = models.CharField(max_length=25, blank=False, default=None)
    # phone = models.CharField(max_length=25, blank=True, default=None)
    
    # class Meta:
    #     verbose_name = "User account"
    #     verbose_name_plural = "User accounts"
    
    # def __str__(self):
    #     return f"{self.user}"

