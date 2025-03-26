from django.contrib import admin
from django.urls import path, include
from authentication_app.api.views import RegistrationView, LoginView, BaseInfoView
from profile_app.api.views import ProfileInfoView
from reviews_app.api.views import ListAllReviews

urlpatterns = [
    path('', ListAllReviews.as_view()),
]