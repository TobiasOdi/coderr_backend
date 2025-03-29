from django.contrib import admin
from django.urls import path, include
from authentication_app.api.views import RegistrationView, LoginView, BaseInfoView
from profile_app.api.views import ProfileInfoView
from reviews_app.api.views import ListAndCreateReviews, UpdateDeleteOwnReview

urlpatterns = [
    path('', ListAndCreateReviews.as_view()),
    path('<int:review_id>/', UpdateDeleteOwnReview.as_view()),
]