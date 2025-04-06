from rest_framework import status
from rest_framework.exceptions import APIException
from datetime import datetime
from django.contrib.auth.models import User
from offers_app.models import UserDetails



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

    if creator_id is not None:
        queryset = queryset.filter(business_user=creator_id)
    elif min_price is not None:
        queryset = queryset.filter(min_price__egt=min_price)
    elif max_delivery_time is not None:
        queryset = queryset.filter(min_delivery_time__lte=max_delivery_time)
        return queryset
    else:
        return queryset
    
def get_additional_field_data(self):
    # user=self.request.user
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    u = User.objects.get(pk=15)
    userdata = User.objects.filter(pk=15).values()
    print("USEDATA", userdata)
    user_details = UserDetails.objects.create(
            user=u,
            first_name=userdata[0]["first_name"],
            last_name=userdata[0]["last_name"],
            username=userdata[0]["username"]               
    )
    
    return {
        "date": dt_string,
        "user": u,
        "user_details": user_details
    }
        