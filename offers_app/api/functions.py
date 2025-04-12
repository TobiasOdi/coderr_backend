from rest_framework import status
from rest_framework.exceptions import APIException
from datetime import datetime
from django.contrib.auth.models import User



class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: str(detail)}
        else: self.detail = {'detail': str(self.default_detail)}

def filtered_queryset(self, queryset):
    creator_id = self.request.query_params.get('creator_id')
    min_price = self.request.query_params.get('min_price')
    max_delivery_time = self.request.query_params.get('max_delivery_time')

    if creator_id:
        new_queryset = queryset.filter(user=int(creator_id))
        return queryset.filter(user=int(creator_id))
    elif min_price:
        return queryset.filter(min_price__egt=int(min_price))
    elif max_delivery_time:
        return queryset.filter(min_delivery_time__lte=int(max_delivery_time))
    else:
      return queryset
    
def get_additional_field_data(self):
    user=self.request.user
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    # u = User.objects.get(pk=user.pk)
    u = User.objects.get(email="tobias@business.ch")
    # userdata = User.objects.filter(pk=user.pk).values()
    userdata = User.objects.filter(pk=u.pk).values()
    # print("USEDATA", userdata)  

    return {
        "date": dt_string,
        "user": u,
    }
        