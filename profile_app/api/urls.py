from django.contrib import admin
from django.urls import path, include
from authentication_app.api.views import RegistrationView, LoginView
from profile_app.api.views import ProfileInfoView, ListAllCustomer, ListAllBusiness

urlpatterns = [
    path('<int:pk>/', ProfileInfoView.as_view()),
    path('business/', ListAllBusiness.as_view()),
    path('customer/', ListAllCustomer.as_view()),

]