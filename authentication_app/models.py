from django.db import models

# USER_TYPE = {
#     "customer": "customer",
#     "business": "business",
# }

#username = models.OneToOneField(User, on_delete=models.CASCADE) # vom Auth user model
#email = models.CharField(max_length=25, blank=False, default=None) # vom Auth user model
#password = models.CharField(max_length=25, blank=False, default=None) # vom Auth user model  

# class UserAccount(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) 
#     type = models.CharField(max_length=50, choices=USER_TYPE,blank=False)
    
#     def __str__(self):
#         return f"{self.user}"

