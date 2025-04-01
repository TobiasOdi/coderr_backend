from django.db import models
from django.contrib.auth.models import User

USER_TYPE = {
    "customer": "customer",
    "business": "business",
}
class Profile(models.Model):
    # auth_user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False, editable=False, default=13)
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

    
    # Für das features feld muss die Liste in einen String umgewandelt werden:
    # In [3]: json.dumps([[1, 3, 4], [4, 2, 6], [8, 12, 3], [3, 3, 9]])
    # Out[3]: '[[1, 3, 4], [4, 2, 6], [8, 12, 3], [3, 3, 9]]'
    # You can add a method into your class to convert it automatically for you.
    # import json

    # class Foobar(models.Model):
    #     foo = models.CharField(max_length=200)

    #     def set_foo(self, x):
    #         self.foo = json.dumps(x)

    #     def get_foo(self):
    #         return json.loads(self.foo)
