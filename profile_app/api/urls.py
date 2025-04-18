from django.urls import path
from profile_app.api.views import ProfileInfoView, ListAllCustomer, ListAllBusiness

urlpatterns = [
    path('<int:pk>/', ProfileInfoView.as_view()),
    path('business/', ListAllBusiness.as_view()),
    path('customer/', ListAllCustomer.as_view())
]